# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:55:55 2016

@author: JJALAW
"""
import matplotlib.pyplot as plt

#lINE AND SCATTER PLOTS
#Lists of years and populations
year = [1950, 1970, 1990, 2010] 
pop = [2.519e10, 3.692e10, 5.263e10, 6.972e10] 

#Build a line plot
plt.plot(year, pop)
plt.show()

#Build a scatter plot
plt.scatter(year, pop)
plt.show()

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

#HISTOGRAMS - if you do not specify Bins, then Python by default picks 10 bins.
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6] 
plt.hist(values,bins = 3)
plt.show() 

# Build histogram with 5 bins
plt.hist(values,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 13 bins
plt.hist(values,bins=13)

# Show and clean up again
plt.show()
plt.clf()

