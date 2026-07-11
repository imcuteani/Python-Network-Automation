# Python requests library with HTTP requests and web resources. 

# The python requests module comes with GET, POST, PUT, DELETE HTTP operations. 
# HTTP GET is to retrieve the contents from REST API 

# parameters are used - 
# 1. url -> The URL you would like to send to (required)
# 2. params -> Dictionary or bytes to be sent in the query string for GET requests (optional)
# 3. **kwargs -> Additional optional arguments such as headers, cookiesm authentication, timeout, proxies etc. 
# Return type -> response object 
# 
# Make a simple GET request 
# 

import requests
response = requests.get("https://www.google.com")
print(response.status_code) 

# sending GET request with Parameters 

import requests
response = requests.get("https://api.github.com/users/imcuteani")
print(response.status_code)
print(response.content)

# HTTP Response objects 
# 1. response.headers -> returns a dictionary of response headers. 
# 2. response.encoding -> response encoding returns the encoding used to decode the response content 
# 3. response.elapsed -> returns a timedelta object with the time elapsed from sending the request and arrival of the response. 
# 4. response.close() -> close the connection to the server 
# 5. response.content() -> returns the content of the response in bytes. 
# 6. response.cookies -> returns the cookiejar object with the response cookies sent back from the server 
# 7. response.history -> returns a list of response objects holding the history of requests. 
# 8. response.json() -> returns a list of JSON objects of the result. 
# 9. response.url -> returns the URL of the response. 
# 10. response.text -> returns the content of the response in unicode. 
# 11. response.reason -> returns the text corresponding to the status code 
# 12. response.links -> returns the header links
# 13. response.ok -> returns True if the status code is < 400 and >= 200. Otherwise return False.  