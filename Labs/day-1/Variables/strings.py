# python String methods 
# In python, a method is the function associated with an object which lets you to perform 
# specific actions on that object. 

# string methods create a new string and leave the original string unchanged. To keep the result. you 
# need to assign it to a new variable or overwrite the original one. 

my_var = "cisco-router"
my_var = my_var.upper()
print(my_var)

# the .split() method in python strings breaks down the strings into smaller ones. It splits the string at spaces,
# turns the sentence into individual words and returning them as a list. 

router_def = "Thisis the basic information about cisco and juniper routers"
words = router_def.split()
print(words)

ip_addr = "172.16.1.11"
components = ip_addr.split(".")
print(components)

# The join method in python is the opposite of .split() method. It lets you to merge a list of strings into
# one string. This is useful for creating strings with custom seperators. 

octets = ['172', '10', '21', '15']
formatted_address = ".".join(octets)
print(formatted_address)

# The python string method consists of .strip() method which removes the leading and trailing
# whitespace from a string. This includes the spaces, tabs, and newline characters. 

#sentence= 
cleaned_sentence = " In the switch thereare various components. ".strip()
print(cleaned_sentence)

# replaces entire spaces from the python string 
cleaned_sentence = "Hello Python  Ntwork Automation with Strings"
replacd_spaces = cleaned_sentence.replace(" ","")
print(replacd_spaces)
