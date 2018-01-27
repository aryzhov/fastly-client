### Fastly Python Billing and Stats Client

The Fastly API client (api.fastly.com) that supports billing and stats. 

Developed using marshmallow (for serialization) and requests (for REST API calls).

## Example

```python
from fastly import client

fastly = client.FastlyClient('your-api-token')

month = client.month(2017, 12)

bill = fastly.bill(month)

regions = fastly.regions(month)

services = fastly.services()

stats = fastly.service_stats(month, services[0].id, regions[0])
```