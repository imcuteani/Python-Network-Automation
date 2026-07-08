# exception handling in Python

# Python relies on four distinct blocks to test, catch and clean up errors. 

# 1. try() block -> wraps the risky block of code that might raise an error. 
# 2. except() block -> executes if an error occurs inside the matching try block
# 3. else() block -> runs only if the code inside the try block executes without any error 
# 4. finally() block -> runs no matter what, it makes it ideal for cleanup tasks like closing of opened files. 
# 
try:
    file = open("data.txt", "r") 
    content = file.read()
    result = 10 / int(content)
except FileNotFoundError:
    print("Error: The specified file doesn't exist in the directory")
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: Could not convert data to an integer")
else:
    print("Data processed successfully")
    print(f"result: {result}")
finally:
    try:
        file.close()
        print("File resources successfully closed")
    except NameError:
        pass                        