# In python, a tuple is a way to store the collection of items which are in a specific order. 
# tuples are similar to lists, but they have some differences with list. 

# a tuple is collection of items which are ordered and can be different types. you can create tuple using 
# parenthesis() with items seperated by commas. 

my_ip = ("1.1.1.1", "switch", 22, None, 5.7)
print(type(my_ip))

# accessing the elements from tuples 

print(my_ip[3])

# real time scenarios to consider python tuples instead of python list 

# if you have fixed collection of router IP address, vlan Ids, that shouldn't change 

# when the collection size wont change during the code execution. 

# when you need to store data of heterogenous data type and when the data represents a heterogeneous concept. 

# add single items to tuple (type conversion) 

ip_address = ("10.10.1.1", "10.10.1.2")

# convert it to list

ip_list = list(ip_address)

# add items in the list 

ip_list.append("10.10.1.3")
ip_list.append("10.10.1.4")

# convert back the list to tuple again 

new_ip = tuple(ip_list)
print(new_ip)

# direct concatenation with list mutation 

# if you would need to combine a list a tuple into a new tuple without explicit modification of a temp list. 
# convert the list directly into a tuple and add them together with the + operator. 

ip_tuple = ("10.10.1.1", "10.10.1.2")
ip_list = ["0.0.0.0", "1.1.1.1"]

#Convert directly from list to tuple and concatenate 

new_tuple = ip_tuple + tuple(ip_list)

print(new_tuple)

