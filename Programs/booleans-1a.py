# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:43:33 2016

@author: JJALAW
"""

# Comparison of booleans
print(True==False)

# Comparison of integers
print(-5*15!=75)

# Comparison of strings
print("pyscript"=="PyScript")

# Compare a boolean with an integer
print(True==1)

# Comparison of integers
x = -3 * 6
x = -3 * 6
print(x>=-10)

# Comparison of strings
y = "test"
print("test"<=y)

# Comparison of booleans
print(True>False)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen<3*your_kitchen)

#The "not" statement
x = 8
y = 9
print(not(not(x < 3) and not(y > 14 or y > 10)))

#The "if" statement
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")
# if-else construct for area
if area > 15 :
    print("big place!")

else:
    print("pretty small.")

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area>10:
    print("medium size, nice!")
else :
    print("pretty small.")
    
