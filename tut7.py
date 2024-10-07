#Functions in python 
# types of functions - 2 types built in functions and user defined functions
def function1():
    print("This is a function")

def addition(value1,value2):
    return value1+value2

def display(start,end):
    for i in range(start,end+1):
        print(i)

# default valued parameters
def greet(name="Human"):
    print(f"Hello {name}")
    return

# recursion
def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

print(factorial(5))