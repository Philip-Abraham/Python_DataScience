# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 08:45:34 2016

@author: JJALAW
"""

import numpy
x=numpy.array([1, 2, 3])
print(x)
print(type(x))
print(3*x)

#Import the numpy package as np, so that you can refer to numpy with np.
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


#BASEBALL PLAYER PHYSICAL ATTRIBUTES DATA
# height and weight are available as a regular lists
height=[78,75,72,79]
weight=[220,180,270,190]


# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
print(bmi)

# Create a boolean Numpy array: the element of the array should be True if the 
#corresponding baseball player's BMI is below 25. 
#You can use the < operator for this. Create the normal_Bmi array.
normal_Bmi=bmi<25

# Print out normal_Bmi
print(normal_Bmi)

# Print out BMIs of all baseball players whose BMI is below 25
print("These are the acceptable BMI values", bmi[normal_Bmi])

#Subset np_weight_kg: print out the element at index 2.
print(np_weight_kg[2])

#Print out a sub-array of np_height: 
#It contains the elements at index 0 up to and including index 2
print(np_height_m[0:3])

# Create baseball, a list of lists. 
#List containing the height and the weight of 4 baseball players
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Create a 2D Numpy array from baseball: np_baseball
np_baseball=np.array(baseball) 
print(np_baseball)    

# Print out the type of np_baseball
print(type(np_baseball)) 

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print the dimensions of np_baseball array
print(np_baseball.ndim) 

# Print out the 3rd row of np_baseball
print(np_baseball[2,:])

# Print out the entire second column of np_baseball: np_weight
np_weight=np_baseball[:,1]
print(np_weight)

# Print out height of 4th player
print(np_baseball[3,0])

#>>>>>SOME STATISTICS<<<<<<
# Create np_height from np_baseball
np_height=np_baseball[:,0]

# Print mean height (first column)
avg = np.mean(np_height)
print("Average: " + str(avg))

# Print out the median of np_height
med = np.median(np_height)
print("Median: " + str(med))

# Print out the standard deviation on height.
stddev = np.std(np_height)
print("Standard Deviation: " + str(stddev))

# Print out correlation between height(1st col) and weight (2nd col) columns. 
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
      