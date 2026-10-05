# python functions with parameters
# parameters are values that get passed as arguements when invoke a function.

def greeting(name):
 print(f"Hello {name}.Hope you are doing fine?")

greeting("Walii")
greeting("Mariam")
greeting("leila")
greeting("Ally")

# below is an addition function that accepts 3 parameters
def add (x,y,z):
 sum=x+y+z
 print("The sum of their numbers is",sum)

add(45,20,16)

# by use of a function that accepts parameters calculate the speed of a vehicle which covered 400km in 5 hrs time.speed=distance/time.

def speed(distance,time):
 speed=distance/time
 print("The speed of the vehicle",speed)

speed(400,5)

 