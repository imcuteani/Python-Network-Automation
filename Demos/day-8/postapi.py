# example of HTTP Post request 

import requests
payload = {'username': 'pythonnet', 'password': 'user123'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)

# session object 
# The session object allows to persist certain parameters across the requests. It also persists cookies across all requests 
# made from session instance. Will use urllib3's connection pooling. So that, it can make multiple several requests to the same host. 
# the underlying TCP connection will be reused which can result in a significant performance increase. 

import requests
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)

# session cookie with method level parameter

s = requests.Session()
r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)

r = s.get('https://httpbin.org/cookies')
print(r.text)

# session set with Context Manager 
# the requests.Session object can be used as a context manager using Python's with statement. 
# This pattern ensures that the system automatically closes the session and releases underlying network connections as soon as 
# execution leaves the indentation block. Even if your code encounters unhandled exception. 

# Benefits 
# 1. Automatic cleanup -> eliminates the need of manual invoke of session.close()
# 2. connection pooling -> reuses the same TCP connection for multiple requests to the same host. 
# 3. state persistance -> automatically stores and manages cookies, default headers, authentication config and sequential requests. 
# 4. exception safety -> the network resources are handled safely freed if an exception is raised with the with block. 

import requests
# the context manager automatically opens ans cleans up the session

with requests.Session() as session:
    session.headers.update({"User-Agent": "MyApp/1.0"})

    # all requests inside this block share the same connection pool and cookies 
    response1 = session.get("https://httpbin.org/cookies/set/sessioncookie/1234567890")
    response2 = session.get("https://httpbin.org")

    print(response1.text)
    print(response2.text)

# the Session is safely closed here        
