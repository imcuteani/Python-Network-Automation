# lambda functions are small anonymous functions which do not have a defined name. 
# lambda contain only one expression
# result of that expression is returned automatically 

a = 'ciscoxerouter'
upper = lambda x: x.upper()
print(upper(a))

# map(): This function applies a lambda expression to each element and returns a map object. It can be converted to 
# a list(). 

a = [1, 2, 4, 8]
double = map(lambda x: x * 2, a)
print(list(double))

# reduce(): this function repeatedly applies over a lambda expression to elements of a list and combine then into a single result. 

from functools import reduce

a = [10, 20, 40, 60]
multiplication = reduce(lambda x, y: x * y, a)
print(multiplication)

# list comprehension -> lambda function can be combined with python list comprehension to apply the same operation to multiple values in a compact way

func = [lambda arg=x: arg * 10 for x in range(1,5)]
for i in func:
    print(i())


# filter() -> this function uses lambda expression to select elements from a list which can statisfy a given condition. 
# such as keeping only even numbers 

c = [10, 20, 30, 40, 50, 57, 69]
even_numbers = filter(lambda x: x % 2 == 0, c)
print(list(even_numbers))


# conditions checking -> lambda function can use conditional expression (if-else) to return different results 
# based on conditions. 

check_item = lambda x: "Positive" if x > 0 else "Negetive" if x < 0 else "Zero"
print(check_item(10.0334))
print(check_item(-5.3335))
print(check_item(0.000))
