# python module 
#----------------------------------
# a module is a single file containing reusable code while a package is a directory which organizes multiple related modules together 
# in a hiearchical manner. 
# Core component difference 
# python module is a single .py file 
# python package is a file directory (folder)
# python module contains the functions, classes and variables 
# python package contains the sub packages and __init__.py file. 
# python module is based on the file name. (namespace) whereas python package is hiearchical, using .dot notation. 

# python modules using built-in standard library
import math
print(math.pi)

import datetime as dt
today = dt.date.today()

# python package is a directory containing the structures of modules. This directory contains python modules and also 
# having __init__.py file which is the interpreter to interprets it as a package. The package is simply a namespace. 
# the package also contains the sub-packages inside it. 

import pandas as pd
import numpy as np 

data = np.array(['p', 'y', 't', 'h', 'o', 'n'])

ser = pd.Series(data)
print(ser)