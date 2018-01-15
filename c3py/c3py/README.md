# CloudCenter API Wrapper

This API wrapper is a work in progress. It gives the ability to interface with the [CloudCenter API](https://docs.cloudcenter.cisco.com)

## Usage


```python
from c3_api import c3Api
import json

address = "https://10.127.193.138"
user = "cliqradmin"
key = "2A661A771F8B1205"

CloudCenter = c3Api(address,user,key)
#From there, you can work with cloudcenter apis very easily. For example"

print(cloudcenter.policyManagement.viewActionPolicy(2))
```
