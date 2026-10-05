# python functions
# a function is a block of code/statements that perform a given task/action/job.They are reusable meaning after creating a function you can invoke it multiple times.
# we have  main types of functions in python i.e
# 1.IN-BUILT FUNCTIONS=>They come pre-installed with the python interpreter e.g include print(),append(),sort(),pop() etc.

# 2.USER DEFINED FUNCTIONS=>These are functions created by the programmer himself.We use the DEF KEYWORD followed by the name of the function,parentheses and a full colon at the end.On the line that follows,you need to indent which marks the start of the body of the function. 

def greeting():
    print("Hello there.Hope you are doing fine.")

# below we call the function by use of its name 
greeting()

# below is an additional fuction 
def addition ():
    number1=30
    number2=20
    answer=number1+number2
    print("The answer is:", answer)

addition() 

# multiplication function
def multiplication():
    number1=3
    number2=4
    number3=5
    answer=number1*number2*number3
    print("the answer is :",answer)

multiplication()

#  below is a function that accepts user inputs 
def divide():
    number1=int(input("enter the first number:"))
    number2=int(input("enter the second number:"))
    quotient=number1/number2
    print("the answer is",quotient)

divide()    
divide()
divide()    
    

    

 

