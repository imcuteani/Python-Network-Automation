# for loops consists of for keyword 

# contains the loop variable -> in (for ip in ip_list) ip is the temp loop variable, it's a temp variable which represents 
# each itemd in the iterable during the loop cycle. 

# looping object 
# ip_list is the list that we can loop over, ip as the variable takes the value of the next item in the list. 

ip_list = ["10.32.1.1", "10.32.1.2", "10.38.3.1", "10.38.3.2"]
for ip in ip_list:
    print(ip)


# Break statements - Exiting the loop of python

for i in range(10):
    print(i)
    if i == 5:
        break
print(f"last value in the loop--> {i}")   

# Continue statements - Skipping the iteration in a loop 

# The continue statement is used to skip the current iteration of a loop and move to the next one. 
# unlike the break statement, the continue doesn't exit the loop, it just skips the current iteration and goes to the
# next one. 

for i in range(10):
   # print(i)
    if i == 5:
        continue
    print(i)
print(f"outside continuous loop --> {i}")  

for i in 'pythondictionary':
    if i == 'n' or i == 'y':
        continue
    print(i)


# Nested loops 
# 
# # Nesting loops means putting one loop inside another. 
# 
data_centers = [("dc1", "10.1.1.1"), ("dc2", "10.2.2.2")]

for dc, ip in data_centers:
    for i in range(1, 3):
        print(f"{dc} --> {ip}{i}")


# using else with a for loop ** 

# you can add an else block to a for loop. The code inside the else block runs when the loop has gone 
# through all its elements without hitting a break statement. This is useful when you want to do something only
# if the loop finishes completely without stopping early. 

devices = ["cisco", "juniper", "broadcom"]
for dev in devices: 
    if dev == "vmware":
        print("I found Juniper routers")
        break
    else: 
        print("No AWS VPC found in the list")