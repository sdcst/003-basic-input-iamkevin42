#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math



a = float(input("Please enter the height of the cone:  "))
b= float(input("Now enter the radius of the cone:  "))

slantheight = math.sqrt(b**2 + a**2)
sa = math.pi * b * (b + slantheight)

print(f"Your surface area is {sa}")