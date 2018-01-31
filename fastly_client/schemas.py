import marshmallow as mm
import marshmallow.fields as fields
import datetime
from . import models


class Service(mm.Schema):

    class Version(mm.Schema):
        number = fields.Int()
        created_at = fields.DateTime()
        updated_at = fields.DateTime()
        deleted_at = fields.DateTime(allow_none=True)

        @mm.post_load
        def create(self, data):
            return models.Service.Version(**data)

    id = fields.Str()
    name = fields.Str()
    version = fields.Int()
    versions = fields.List(fields.Nested(Version))

    @mm.post_load
    def create(self, data):
        return models.Service(**data)


class Billing(mm.Schema):

    class Region(mm.Schema):

        class Details(mm.Schema):

            class Tier(mm.Schema):
                name = fields.Str()
                units = fields.Number()
                price = fields.Number()
                discounted_price = fields.Number()
                total = fields.Number()

                @mm.post_load
                def create(self, data):
                    return models.Invoice.Region.Details.Tier(**data)

            total = fields.Number()
            tiers = fields.List(fields.Nested(Tier))

        class Bandwidth(Details):

            @mm.post_load
            def create(self, data):
                return models.Invoice.Region.Bandwidth(**data)

        class Requests(Details):
            @mm.post_load
            def create(self, data):
                return models.Invoice.Region.Requests(**data)

        bandwidth = fields.Nested(Bandwidth)
        requests = fields.Nested(Requests)
        cost = fields.Number()

        @mm.post_load
        def create(self, data):
            return models.Invoice.Region(**data)

    start_time = fields.DateTime()
    end_time = fields.DateTime()
    invoice_id = fields.Raw()
    regions = fields.Dict(values=fields.Nested(Region))

    @mm.post_load
    def create(self, data):
        return models.Invoice(**data)


class ServiceStats(mm.Schema):

    class Daily(mm.Schema):
        service_id = fields.Str()
        start_time = fields.Function(deserialize=lambda n: datetime.datetime.fromtimestamp(n))
        bandwidth = fields.Number()
        requests = fields.Number()

        @mm.post_load
        def create(self, data):
            return models.Stats.DailyStats(**data)

    class StatsMeta(mm.Schema):
        region = fields.Str()

        @mm.post_load
        def create(self, data):
            return data["region"]

    data = fields.List(fields.Nested(Daily))
    meta = fields.Nested(StatsMeta)

    @mm.post_load
    def create(self, data):
        return models.Stats(daily_stats=data["data"], region=data["meta"])


class StatsRegions(mm.Schema):

    data = fields.List(fields.Str())

    @mm.post_load
    def create(self, data):
        return data["data"]
