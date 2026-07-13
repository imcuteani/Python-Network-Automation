# custom python classes with __str__() and __repr__() methods
# 
# built-in datetime classes to show up the difference between __str__()and __repr__() methods.
# 
import datetime 

# creating a datetime object 
mydate = datetime.datetime(2026, 7, 9, 10, 00, 00, 42056)

# using the str() calls __str__() 

print("str() output", str(mydate))
print("print() output:", mydate)

# using repr() calls __repr() 

print("repr() output:", repr(mydate))
print("REPL output:", mydate)  # in REPL, this shows repr()

# Real time scenarios 

# use the __str__() when:
# display data to end users in UI or reports the str() methods by wrapping the object output from str() constructor to str() method
# create user-friendly error message
# logging information for non-technical stakeholders 
# building CLI applications with user output 
