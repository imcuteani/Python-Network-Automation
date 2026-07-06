# Program to show the simple interest 

def simple_interest(p, t, r):
    print("The principal is: ", p)
    print("The time period is: ", t)
    print("The rate of interest is: ", r)

    interest_val = (p * t * r)/100


    print("The simple interest is: ", interest_val)

    #Driver code

    simple_interest(1000, 2, 8)
