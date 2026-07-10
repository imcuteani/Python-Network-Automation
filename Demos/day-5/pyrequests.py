# sending a request -> to make a GET request, you can use the Get() method and pass the URL. 

import requests 
response = requests.get("https://google.com")

print(response.text)

# post request 

data = {"device": "Router", "ipaddress_type": "IPv4"}
response = requests.post('https://httpbin.org/post', json=data)

# view results 

print(response.status_code)
print(response.json)             # parse the output as json format 


import requests 

try: 
    response = requests.get("https://google.com/india/invalid-url")
    response.raise_for_status()
except requests.exceptions.HTTPError as err: 
    print(f"Request has failed: {err}")    


# Simple Retry mechanism with Python 
# 
from requests.adapters import HTTPAdapter 
from urllib3.util import Retry

#1. define the configuration for retrying failed requests 

retry_strategy = Retry(
    total=3,     # Max 3 total retry attempts
    backoff_factor=1,  #wait 1s, 2s, 4s.. between attempts
    status_forcelist=[500, 502, 503, 504], # Status codes that triggers a retry
    allowed_methods=["GET", "POST"] # HTTP methods to retry
    
)

# 2. pass the strategy to HTTPAdapter
adapter = HTTPAdapter(max_retries=retry_strategy)

# 3. attach the adaptor to a session instance 
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

#4. Make requests using the session
try: 
    response = session.get("https://httpbin.org/status/503")
    print(f"Status code: {response.status_code}")
except requests.exceptions.RetryError as e:
    print(f"Failed after max retries: {e}")    

