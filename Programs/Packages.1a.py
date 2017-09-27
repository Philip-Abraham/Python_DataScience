# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2*(math.pi)*r

# Calculate A
A = (math.pi)*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

#Selective import
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon if 12 degrees. Store in dist.
dist=r*radians(12)

# Print out dist
print(dist)

#Different ways of importing
#There are several ways to import packages and modules into Python.
#Depending on the import call, you'll have to use different Python code.
#Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package.
#You want to be able to use this function as follows: 
#my_inv([[0,-1,1,0], [2,1,0,2],[1,-1,3,0],[0,1,1,-1]])
#You will use the following scipy import statement in order to run the above code without an error?

from scipy.linalg import inv as my_inv
my_inv([[0,-1,1,0], [2,1,0,2],[1,-1,3,0],[0,1,1,-1]])

