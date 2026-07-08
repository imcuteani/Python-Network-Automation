# dictionary is a data structure which stores the information in key-value pairs. While keys must be unique and 
# immutable (like strings or numbers) values can be of any data type. This makes dictionaries ideal for accessing data by a specific 
# name rather than a numeric position like in list. 

ip_list = {"subnet_1": "10.10.1.1", "subnet_2": "10.10.1.2" }
print(type(ip_list))

# accessing items within the dictionary, a value in dictionary is accessed by using the key. This can be done with square brackets [] 
# or with get() method. Both return the value linked to the given key. 

print(ip_list["subnet_1"])            # access using Key
print(ip_list.get("subnet_2"))        # access using get()  

# new items can be added to the dictionary using the assignment operator (=) by giving a new key a value. If an existing 
# key is used with an assignment operator, its value is updated with new one. 

ip_list["subnet_3"] = "10.10.1.3"
ip_list["subnet_1"] = "192.168.1.1"
print(ip_list)

# Removing of Dictionary items 
# Dictionary items can be removed using the built-in deletion method. 

#1. del() method -> removes an item using its key 

del ip_list["subnet_3"]
print(ip_list) 

# 2. pop() -> removes the item with the given key and returns the value. 
val = ip_list.pop("subnet_1")
print(val)
print(ip_list)

#3. .popitem() -> removes and return the last item from the dictionary as inserted key-value pair. 

ip_list = {"subnet_1": "10.10.1.1", "subnet_2": "10.10.1.2", "subnet_3": "10.10.1.3", "subnet_4": "10.10.1.4" }
print(ip_list.popitem())

#4. clear() -> removes all items from the dictionary 
# removes all items from dictionary
ip_list.clear() 
print(ip_list)

# Iteration through the dictionary 

# A dictionary can be traversed using the for loop to access its key, values or both key-value pairs. Dictionary in python
# has built-in method keys(), values() and items(). 

#1. iterate keys -> return all keys from dictionary 
ip_list = {"subnet_1": "10.10.1.1", "subnet_2": "10.10.1.2", "subnet_3": "10.10.1.3", "subnet_4": "10.10.1.4" }
for ip in ip_list:
    print(ip)

#2. iterate values -> return all values from dictionary 
ip_list = {"subnet_1": "10.10.1.1", "subnet_2": "10.10.1.2", "subnet_3": "10.10.1.3", "subnet_4": "10.10.1.4" } 
for ip in ip_list.values():
    print(ip) 

#3. iterate over key-value pairs -> return all key-value pairs as tuples. 
# return all ips from subnets
ip_list = {"subnet_1": "10.10.1.1", "subnet_2": "10.10.1.2", "subnet_3": "10.10.1.3", "subnet_4": "10.10.1.4", "subnet_5": "10.10.1.5" }
for ip, subnet in ip_list.items():
    print(ip, subnet)       
