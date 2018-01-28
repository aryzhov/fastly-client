
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
        def __init__(self, bandwidth, requests, cost, discount=0, **kwargs):
            self.bandwidth = bandwidth
            self.requests = requests
            self.cost = cost
            self.discount = discount

    def __init__(self, invoice_id, start_time, end_time, regions, **kwargs):
        self.invoice_id = invoice_id
        self.start_time = start_time
        self.end_time = end_time
        self.regions = regions


class Stats(object):

    class DailyStats(object):
        def __init__(self, service_id, start_time, bandwidth, **kwargs):
            self.service_id = service_id
            self.start_time = start_time
            self.bandwidth = bandwidth

    def __init__(self, daily_stats, region, **kwargs):
       self.daily_stats = daily_stats

