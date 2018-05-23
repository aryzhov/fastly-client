import requests
from urllib import parse as urlparse
from . import schemas
from . import models
from datetime import datetime, timezone
from marshmallow import exceptions as mm_exc

def add_months(year, month, months):
    mm = month + months - 1
    return year + mm // 12, mm % 12 + 1


def period(year, month, months=1):
    date1 = datetime(year, month, 1, tzinfo=timezone.utc)
    year2, month2 = add_months(year, month, months)
    date2 = datetime(year2, month2, 1, tzinfo=timezone.utc)
    return (date1, date2) if months > 0 else (date2, date1)


class FastlyException(Exception):

    def __init__(self, status=None, message=None, errors=None):
        self.status = status
        self.message = message
        self.errors = errors

    def __str__(self):
        result = []
        if self.status:
            result.append("HTTP response: {}".format(self.status))
        if self.errors:
            result.append("Parse errors: {}".format(self.errors))
        if self.message:
            result.append(self.message)
        return ", ".join(result)


class Client(object):

    def __init__(self, auth_token, url="https://api.fastly.com"):
        self._base_url = url
        self._auth_token = auth_token

    def _get(self, path, schema, many, params=None):
        url = urlparse.urljoin(self._base_url, path)
        headers = {"Fastly-Key": self._auth_token,
                   "Accept": "application/json"}
        response = requests.get(url, params=params, headers=headers)
        try:
            response.raise_for_status()
        except (requests.HTTPError, requests.exceptions.ConnectionError) as e:
            raise FastlyException(status=response.status_code, message=response.text)
        try:
            result = schema.loads(response.text, many=many)
            return result
        except mm_exc.ValidationError as ex:
            raise FastlyException(errors=ex.messages)

    def services(self):
        return self._get("service", schema=schemas.Service(), many=True)

    def bill(self, period):
        return self._get("billing/v2/year/{}/month/{}".format(period[0].year, period[0].month), schema=schemas.Billing(), many=False)

    def regions(self, period):
        params = {"from": int(period[0].timestamp()),
                  "to": int(period[1].timestamp())}
        return self._get("stats/regions", schema=schemas.StatsRegions(), many=False, params=params)

    def service_stats(self, period, service_id, region):
        params = {"from": int(period[0].timestamp()),
                  "to": int(period[1].timestamp()),
                  "by": "day"}
        if region:
            params["region"] = region
        return self._get("stats/service/{}".format(service_id), schema=schemas.ServiceStats(), many=False, params=params)
