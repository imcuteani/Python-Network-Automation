# Classes & objects in python difference 

# Classes are the blueprint for creating objects & objects are instance of a class
# Defines the attributes and methods whereas the object uses attributes and methods 
# classes are created using class keyword and objects are created by calling the class 

# __init__() methods to initialize objects 
# it acts as a constructor and is automatically executed when an object is created. It is used to initiate the attributes 
# of the object with the values provided at the time of object creation. 

# A constructor is method which runs automatically where a new object is created. It assigns initial values to the object properties. 

# The self keyword -> represents the specific instance of the object which you are working with. You should include it 
# as the first parameter of any instance methods so that Python can track the object to modify. 

# Attributes vs methods -> attributes are the variables which hold the data inside the class. Methods are the functions inside the
# class that define what the object can do. 

# classes and instance variables -> class attributes which are shared equally by all instances, instance attributes are unique to each individual object. 

class Router:
    devices = "Cisco"   # class attribute

    def __init__(self, device_ip, manufacturer):
        self.device_ip = device_ip # instance attribute
        self.manufacturer = manufacturer # instance attribute

# create the object with the Router class
router1 = Router("10.10.1.1", "Cisco_IOS")

print(router1.device_ip)       # accesses the object's instance attribute
print(router1.devices)         # invokes the class attribute


# __str__() method allows us to define a custom string representation of an object. By default, when we print an object or convert it 
# to a string using the str(), python uses the default implementation which returns a string like <__main__.ClassName object 0x000000123>. 

class Router:
    devices = "Cisco"   # class attribute

    def __init__(self, device_ip, manufacturer):
        self.device_ip = device_ip # instance attribute
        self.manufacturer = manufacturer # instance attribute

        def __str__(self):    # defines a method in Router class, uses the self parameter to access the instance attributes. 
            return f"{self.device_ip} and {self.manufacturer} of the Router"
 
router1 = Router("10.10.1.1", "Cisco_IOS")
router2 = Router("10.10.1.2", "Arista Switches")

print(router1)
print(router2)


