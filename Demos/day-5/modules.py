# built-in modules -> pre-installed utilizes bundled into standard installer. (math, os, sys, random)
# user-defined modules -> created by you for specific project purposes and utilized multiple projects per logic
# 3rd-party modules -> PyPI (numpy, pandas, requests, sockets)

# built-in module 

import math
print(math.sqrt(16)) # requires prefixing with module name 

# 2. for importing specific attributes or functions

from math import pi, factorial
print(factorial(5))  # directly available without prefixing

import random as rd 
print(rd.randint(1, 10))

# use custom python module 

import ipcalculator

addition_result = ipcalculator.add(5, 6)
print(addition_result)

subs_result = ipcalculator.subs(10, 5)
print(subs_result)

mul_result = ipcalculator.mul(20, 4)
print(mul_result)

div_result = ipcalculator.div(30, 3)
print(div_result)

# 3rd-party python modules 
# For HTTP web development and HTTP1.1 and 2.0 requests with Python. 

# send requests with parameters, headers, cookies and authentication. It supports data into various formats like JSON, XML and form data. 
