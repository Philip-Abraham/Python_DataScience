# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:22:59 2016

@author: JJALAW
"""


import numpy

positions=loadtxt("C:/Users/Philip Abraham/OneDrive/TECHNOLOGY/Data Analysis/Data/positions.txt",str)
np_positions=numpy.array(positions)
print(np_positions)
type(np_positions)
print("number of data points=",len(np_positions))

heights=loadtxt("C:/Users/Philip Abraham/OneDrive/TECHNOLOGY/Data Analysis/Data/heights.txt",str)
np_heights=numpy.array(heights)
print(np_heights)
type(np_heights)
print("number of data points=",len(np_heights))

# Heights of the goalkeepers: gk_heights
gk_heights=heights[positions=="GK"]

# Heights of the other players: other_heights
other_heights=heights[positions!='GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(numpy.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(numpy.median(other_heights)))