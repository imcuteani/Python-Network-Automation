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