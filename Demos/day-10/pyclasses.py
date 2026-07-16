# Python has the benefits of Object oriented programming which allows a class to inherit attributes and methods from 
# another class. (parent / base class)

# a base class called device which has a method called type(), then there's a child class called router which is created that
# inherit from device class and add their own behaviour. 

class Device:                        # base class in inheritance
    def __init__(self, name):
        self.name = name  # instance variable


        # method of the class 
        def info(self):
            return f"This is a {self.name}."

class Router(Device): 
   def __init__(self, name, cidrs):
      #super() initializes the parent class attributes
      super().__init__(name)
      self.cidrs = cidrs  # specific instance of the router sub class               
    # sub class in inheritance     
    
    # Method overriding: replacing the parent class behaviour
   def info(self):
      return f"This is a {self.name} {self.cidrs} with Router Device Info"


   def feature(self):
       print(self.name, "Aruba Networks")

r = Router("Cisco IOS XE", "10.10.1.1") 
# inherited method
r.info()          # parent method
r.feature()       # child method             
    