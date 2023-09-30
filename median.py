"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median = int((len(numbers)-1) /2)

if len(numbers)%2 == 1: 
    med = int(numbers[median])
    print(float(med))   
else: 
    print((numbers[median]+numbers[median+1])/2)

    


