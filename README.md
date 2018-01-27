### Fastly Python Billing and Stats Client

The Fastly API client (api.fastly.com) that supports billing and stats. 

Developed using marshmallow (for serialization) and requests (for REST API calls).

## Example

```python
import fastly

client = fastly.Client('your-api-token')

month = fastly.month(2017, 12)

bill = client.bill(month)

regions = client.regions(month)

services = client.services()

stats = client.service_stats(month, services[0].id, regions[0])
```