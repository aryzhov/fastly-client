===
Fastly Python Billing and Stats Client
===

The Fastly API client (api.fastly.com) that supports billing and stats.

Developed using marshmallow (for serialization) and requests (for REST API calls).

GitHub: `http://github.com/aryzhov/fastly-client`

Example
=======

::

    import fastly

    client = fastly.Client('your-api-token')

    period = fastly.period(2017, 12, months=1)

    bill = client.bill(period)

    regions = client.regions(period)

    services = client.services()

    stats = client.service_stats(period, services[0].id, regions[0])
