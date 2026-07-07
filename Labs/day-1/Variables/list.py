# Python program to show up a list

nums = []

# appending data to list

nums.append(45)
nums.append(3.2)
nums.append("New Data")

print(nums)

# A list is a basic and flexible way to store collection of items. Lists can hold different types of data,
# like strings, booleans, and even other lists. 

# List is a collection of items 

# Which maintains order -> The order in which you add items is the order in which you can access them
# Holds mixed data types -> you can mix different data types in a single list like string, numbers and more
# Mutable -> you can change the items, size and structure of a list after creating it. 

# creation of list 

my_ip = ["ip", 100, "vlan", [], None, 20.5]
print(type(my_ip))

# List uses zero-based indexing

first_ip = my_ip[1]
print(first_ip) 

# since the lists are mutable, you can change the content of a list, 

my_ip[0] = "10.1.1.1"
print(my_ip)


# Accessing the last element of the list 

# you can use the negetive indices to access the items from the end of list. -1 is the last item, 
# -2 is the second to last item and so on. 

last_element = my_ip[-3]
print(last_element)

# find the length of the list 

# to find out the how many items are in the list, you can use the len() function, this function gives you the number of 
# elements in the list. 

my_list = [20, 40, 60, 10, 34]
list_length = len(my_list)
print("The length of the list is:", list_length)

# range function in python list helps to create a sequence of numbers. By default, range starts at 0 
# and goes up the specified stop value. For example, to create a list of numbers from 0 to 4. 

numbers = list(range(5))
print(numbers)

numbers = list(range(2, 8))
print(numbers)

# In the python range() function, the Step parameters (most efficient) to generate even numbers

# The range() function takes three arguments start, stop (exclusive) and step. 

even_numbers = list(range(0, 20, 2))
print(even_numbers)   # generate even numbers

# generate odd numbers with range function 

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
