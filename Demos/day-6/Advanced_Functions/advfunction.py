# map() function 

# The map() function applies a specified function to each element of an iterable (such as list, tuple or string)
# and returns a new iterable with the modified elements. 

def get_lengths(words):
    return map(len, words)

words = ['cisco', 'juniper', 'arista', 'junos', 'aruba', 'paloalto']
lengths = get_lengths(words)
print(lengths)

# map() function to multiply lists 

def multiply(x, y):
    return x * y

a = [4, 6, 8]
b = [10, 20, 30]
result = map(multiply, a, b)
print(result)

# The reduce() function is part of functool module in python & allows you to apply a function to a sequence of element in order to reduce them to a single value. 

# use reduce() method to multiply the elements of a list 

from functools import reduce 

def multiply(x, y):
    return x * y

a = [100, 200, 145, 234]
result = reduce(multiply, a)
print(result)

def add(x, y):
    return x + y

a = [100, 200, 145, 234]
result = reduce(add, a, 0)
print(result)

# zip method combines multiple iterables into a single iterable of tuples. 

a = [10, 20, 30]
b = ['cisco', 'juniper', 'fortinet']
zipped = zip(a, b)
print(tuple(zipped))

# enumerate () function adds a counter to an iterable and returns an iterable of tuples where each tuple consists 
# of the counter and returns an interable of tuples, consists of the original element. 

a = ['cisco', 'arista', 'junos']
for i, element in enumerate(a, 1):
    print(f'{i}: {element}')