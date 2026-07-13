# python REST API benefits 

# Securing access to network REST API is critical to prevent unautorized access, data breaches and service disruptions. 
# There are three primary methods - Basic authentication, Tokens and OAuth2. 

# Basic authentication sending the username and password with each API request. typically encoded in base64. 

# curl -u admin:password https://device-id/api/status

# Token based authentication

# more secure and scalable. The process involves first authenticating with credentials to obtain a token, which is then
# used for subsequent API request. 

# POST /api/auth/login
#{
#   "username": "admin",
#  "password": "password"
#}
#Response:
#{
#    "token":"<hexadecimal token>"
#}

# OAuth2 authentication with REST API delegates the access control to an authorization server, issuing access tokens
# with specific scopes and lifetimes. OAuth2 flows - such as auth code or client credentials - allow network automation
# tools to securely access APIs without exposing user credentials. 

# Consuming of REST API 

import requests 

response = requests.get('https://api.github.com')
print(response.status_code)

try:
    response = requests.get('https://api.github.com', timeout=3.0)# times out after 3 sec
except requests.exceptions.Timeout:
    print("The request has timed out")    
