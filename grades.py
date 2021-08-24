# File:        grades.py
# Started:     by Brianna Richardson (& Dr. Gibson)
# Author:      Sachin Saigal
# Date:        10/11/2017
# Section:     20
# E-mail:      saigal1@umbc.edu
# Description: This file contains python code that uses functions to allow 
#              a user to get information about a list of grades entered.

MIN_VAL = 0
MAX_VAL = 100
SENTINEL = -1

###################################################################
# printList() prints out a list, showing the index of each element
# Input:      theList; a list of any types of variables
# Output:     None
def printList(theList):
    #---------------------------------------------------------#
    # your function to print the list (indexes too) goes here #
    #---------------------------------------------------------#
    count = 0 
    while count < len(theList):
          print (theList[count])
          count +=1

###########################################################
# printMin() prints the minimum value in a list of numbers
# Input:     theList; a list of integers and/or floats
# Output:    None
def printMin(theList):
    #-------------------------------------------------------#
    # your function to find and print the minimum goes here #
    #-------------------------------------------------------#
    minT = theList[0] 
    count = 0
    while count < len(theList):
        if ( minT > theList[count]):
            minT = theList[count]
        count +=1
    return ((minT))
###########################################################
# printMax() prints the maximum value in a list of numbers
# Input:     theList; a list of integers and/or floats
# Output:    None
def printMax(theList):
    #-------------------------------------------------------#
    # your function to find and print the maximum goes here #
    #-------------------------------------------------------#
    maxT = theList[0]
    count = 0
    while count < len(theList):
        if( maxT < theList[count]):
            maxT = theList[count]
        count +=1
    return((maxT))



def main():
    gradeList = []
    msg = "Enter a grade (" + str(SENTINEL) + " to quit): "

    grade = int(input(msg))

    # ask the user for grades until they choose to exit
    while(grade != SENTINEL):
        # check beforehand, so we only save valid grades
        if grade >= MIN_VAL and grade <= MAX_VAL:
            gradeList.append(grade)
        else:
            print("\tThe grade", grade, "is invalid")
            print("\tGrades must be between", MIN_VAL, "and", MAX_VAL)

        grade = int(input(msg))

    # call the print function
    #------------------------------------------------------#
    # your code to call the function printList() goes here #
    #------------------------------------------------------#
    printList(gradeList)
    minp = printMin(gradeList)
    print (" The minimum is ", minp) 
    maxp = printMax(gradeList)
    print (" The maximum is ", maxp) 
        
    # print out the minimum and maximum values
    #-------------------------------------#
    # your code to call the two functions #
    # printMin() and printMax() goes here #
    #-------------------------------------#

main()
