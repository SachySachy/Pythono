"""This program is to create a python data analysis app"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

def analysis(lists,bins):
    """analysis"""
    sums = sum(lists)
    length = len(lists)
    mean = sums/length
    stds = mean * mean + length
    print("The statistics for this column are: ")
    print("count = ", sums)
    print("mean = ", mean)
    print("Standard Deviation = " ,stds)
    print("min = ", min(lists))
    print("max = ", max(lists))
    print("The Histogram of this column is now displayed.")
    plt.hist(lists, bins=bins, edgecolor='black')
    plt.show()

def population():
    """Population Data"""
    popapr = []
    popjul = []
    popcha = []
    with open('PopChange.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            popapr.append(int(line[4]))
            popjul.append(int(line[5]))
            popcha.append(int(line[6]))
    print("You have entered Hosuing Data.")
    print("Select the Column you want to analyze: ")
    print("a. Pop Apr 1")
    print("b. Pop Jul 1")
    print("c. Change Pop")
    choice = input(": ")
    bins = []
    while (choice != 'a' and choice != 'b' and choice != 'c'):
        choice = input("Please enter an a or b or c: ")
    if choice == 'a':
        bins = [10000,30000,50000,70000,90000,110000]
        analysis(popapr,bins)
    elif choice == 'b':
        bins = [10000,30000,50000,70000,90000,110000]
        analysis(popjul,bins)
    elif choice == 'c':
        bins = [-7000,-5000,-3000,-1000,0,1000,3000,5000,7000]
        analysis(popcha,bins)

def housing():
    """Hosuing Data"""
    weight = []
    utility = []
    bins = []
    with open('Housing.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            weight.append(float(line[5]))
            utility.append(float(line[6]))
    print("You have entered Hosuing Data.")
    print("Select the Column you want to analyze: ")
    print("a. weight")
    print("b. utility")
    choice = input(": ")
    while (choice != 'a' and choice != 'b'):
        choice = input("Please enter an a or b: ")

    if choice == 'a':
        bins = [0,500,1000,1500,2000,2500,3000,3500,4000]
        analysis(weight,bins)
    elif choice == 'b':
        bins = [0,50,100,150,200,250,300,350,400]
        analysis(utility,bins)

def main():
    """main"""
    print("***** Welcome to the Python Data Analysis App *****")
    choice = 1
    while choice != 3:
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")
        choice = int(input(": "))

        if choice == 1:
            population()
        elif choice == 2:
            housing()
    print("***** Thanks for using the Data Analysis App *****")

if __name__ == "__main__":
    main()
