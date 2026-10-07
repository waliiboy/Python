# python modules
# A module is a python file that contain definitions and structures.Definitions may include variables,functions,loops,etc.
# We need modules to separate a huge chunk of program into smaller and manageable pieces which are easier to understand and work with.
# In python we have 2 main types of modules i.e in-built and user defined modules.

def add():
    number1=20
    number2=50
    sum=number1+number2
    print("the sum is: ",sum)


# below is a function to find the difference of numbers
def subtract():
    numx=int(input("Enter the first number: "))
    numy=int(input("Enter the second number: "))
    difference=numx-numy
    print("The difference is",difference)


# create a python function that is able to calculate the area of a square.import the function on lesson 5b and invoke it there.

def area_of_square():
    s1=int(input("Enter the first side: "))
    s2=int(input("Enter the second side: "))
    area_of_square=s1*s2
    print("The answer is: ",area_of_square)
