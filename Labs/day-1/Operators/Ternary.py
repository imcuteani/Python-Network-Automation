# Program to show the Ternary operator

a = int(input("Enter Number 1:"))
b = int(int("Enter Number 2:"))

print((b, a), [a < b])

# Use Dictionary for selecting an item

print({True: a, False: b} [a < b])

# Print lambda 

print((lambda : b, lambda: a)[a  < b]())