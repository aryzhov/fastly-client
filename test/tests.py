from unittest import TestCase
from fastly_client import schemas
import json


class Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testService(self):
        with open("service.json") as f:
            schema = schemas.Service()
            services = schema.loads(f.read(), many=True)
        self.assertTrue(len(services) > 0)
        service0 = services[0]
        self.assertTrue(service0.id == "61xzpHvsYa8D7RSiXr2m2g")
        self.assertTrue(service0.name == "dev-environment")

    def testBilling(self):
        with open("billing.json") as f:
            schema = schemas.Billing()
            invoice = schema.loads(f.read(), many=False)

        self.assertTrue(invoice.invoice_id == 15266)
        self.assertTrue(invoice.regions["usa"].bandwidth.total > 50)
        self.assertTrue(invoice.regions["usa"].requests.total_units > 0)

    def testStats(self):
        with open("stats_service_usa.json") as f:
            schema = schemas.ServiceStats()
            stats = schema.loads(f.read(), many=False)

        self.assertTrue(stats)
        self.assertTrue(stats.total_bandwidth > 0)
        self.assertTrue(stats.total_requests > 0)
        self.assertTrue(stats.days > 0)
