"""This program creates a menu for the user to navigate and to solve problems"""
import math
from datetime import datetime

#I will need to make a menu program
#A switch state will work perfectly to so
#A random generate password thats (secure)
#calculate and format a percentage
#calculates how many days un til july 4, 2025
#use law of cosines
#calculate the volume of a right circular cylinder
#Exit program

def secure():
    """secure"""
    print("Generating a password")

def percent():
    """percent"""
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    print("Converting to percentage")
    product = (float(numerator)/float(denominator))*100
    print("Here is the percentage: ", product, "%")

def until1():
    """until"""
    print("days until July 4 2025")
    now = datetime.now()
    future = datetime(2025,7,4)
    diff = future - now
    print(diff.days, " number of days")

def triangle():
    """triangle"""
    print("law of cosine")
    linea = float(input("Enter a number for line 1: "))
    lineb = float(input("Enter a number for line 2: "))
    degre = float(input("Enter a number for angle: "))
    total = (linea * linea) + (lineb * lineb)
    value = 2*linea*lineb
    value2 = (math.cos(math.radians(degre)))
    total = total - (value * value2)
    print("The final line equals: ", math.sqrt(total))

def volume1():
    """volume"""
    print("volume of a Right CC")
    height = float(input("Enter height: "))
    radius = float(input("Enter radius: "))
    radius = radius * radius
    volume = (math.pi*radius) * height
    print("the volume is: ", volume)

def main():
    """main"""
    print("")
    print("********************************************")
    userinput = 'a'
    while userinput != 'f':
        print("a. Generate Secure Password ")
        print("b. Calculate and Format a Percentage ")
        print("c. How many days from today until July 4, 2025" )
        print("d. Use the Law of Cosines to calculate the leg of a triangle ")
        print("e. Calculate the volume of a Right Circular Cylinder ")
        print("f. Exit program ")
        userinput = input("Enter a letter: ")
        print("You have selected: " , userinput)

        if userinput == 'a':
            secure()
        elif userinput == 'b':
            percent()
        elif userinput == 'c':
            until1()
        elif userinput == 'd':
            triangle()
        elif userinput == 'e':
            volume1()
        elif userinput == 'f':
            print("Quiting")
        else:
            print("please enter a proper response")

if __name__ == "__main__":
    main()
