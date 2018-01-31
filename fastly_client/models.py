
class Service(object):

    class Version(object):

        def __init__(self, number, created_at, updated_at, deleted_at):
            self.number = number
            self.created_at = created_at
            self.updated_at = updated_at
            self.deleted_at = deleted_at

    def __init__(self, id, name, version, versions, **kwargs):
        self.id = id
        self.name = name
        self.version = version
        self.versions = versions


class Invoice(object):

    class Region(object):

        class Details(object):

            class Tier(object):

                def __init__(self, name, units, price, discounted_price, total, **kwargs):
                    self.name = name
                    self.units = units
                    self.price = price
                    self.discounted_price = discounted_price
                    self.total = total

            def __init__(self, tiers, total, **kwargs):
                self.tiers = tiers
                self.total = total

            @property
            def total_units(self):
                """
                :return: The number of Gigabytes if bandwidth or the number of requests
                """
                return sum([t.units for t in self.tiers])


        class Bandwidth(Details):
            pass

        class Requests(Details):
            pass

        def __init__(self, bandwidth, requests, cost, **kwargs):
            self.bandwidth = bandwidth
            self.requests = requests
            self.cost = cost

    def __init__(self, invoice_id, start_time, end_time, regions, **kwargs):
        self.invoice_id = invoice_id
        self.start_time = start_time
        self.end_time = end_time
        self.regions = regions


class Stats(object):

    class DailyStats(object):
        def __init__(self, service_id, start_time, bandwidth, requests, **kwargs):
            self.service_id = service_id
            self.start_time = start_time
            self.bandwidth = bandwidth
            self.requests = requests

    def __init__(self, daily_stats, region, **kwargs):
        self.daily_stats = daily_stats
        self.region = region

    @property
    def total_bandwidth(self):
        return sum([d.bandwidth for d in self.daily_stats])

    @property
    def total_requests(self):
        return sum([d.requests for d in self.daily_stats])

    @property
    def days(self):
        return len(self.daily_stats)

