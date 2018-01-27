from unittest import TestCase
from fastly import schemas
import json


class Test(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testService(self):
        with open("service.json") as f:
            schema = schemas.Service()
            services, errors = schema.loads(f.read(), many=True)

        self.assertFalse(errors)
        self.assertTrue(len(services) > 0)
        service0 = services[0]
        self.assertTrue(service0.id == "61xzpHvsYa8D7RSiXr2m2g")
        self.assertTrue(service0.name == "dev-environment")

    def testBilling(self):
        with open("billing.json") as f:
            schema = schemas.Billing()
            invoice, errors = schema.loads(f.read(), many=False)

        self.assertFalse(errors)
        self.assertTrue(invoice.invoice_id == 15266)
        self.assertTrue(invoice.regions["usa"].bandwidth > 50)

    def testStats(self):
        with open("stats_service_usa.json") as f:
            schema = schemas.ServiceStats()
            stats, errors = schema.loads(f.read(), many=False)

        self.assertFalse(errors)
        self.assertTrue(stats)
        self.assertTrue(len(stats.daily_stats) > 0)