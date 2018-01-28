======================================
Fastly Python Billing and Stats Client
======================================

The Fastly API client (api.fastly.com) that supports billing and stats.

Developed using marshmallow (for serialization) and requests (for REST API calls).

Example
=======

::

    import fastly_client

    client = fastly_client.Client('your-api-token')
    period = fastly_client.period(2017, 12, months=1)

    try:
        bill = client.bill(period)
        regions = client.regions(period)
        services = client.services()
        stats = client.service_stats(period, services[0].id, regions[0])
    except fastly_client.FastlyException:
        print("An error occurred")
        raise
