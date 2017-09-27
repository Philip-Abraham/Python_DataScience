# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:46:17 2016

@author: JJALAW
"""

#Leap Yearly Global CO2 Emissions: 1952-2008

import matplotlib.pyplot as plt
import numpy

year, emissions = numpy.loadtxt('C:\\Users\Philip Abraham\OneDrive\TECHNOLOGY\Data Analysis\Data\Yearly-CO2_Emissions2.txt', delimiter=',', unpack=True)

#Customized Line Plot of yearly CO2 emissions
plt.plot(year,emissions, label='Loaded from file!')

plt.xlabel('Year')
plt.ylabel('CO2 Emissions')
plt.title('Yearly Global CO2 Emissions_1952-2008')
plt.legend()
plt.show()

#Customized Scatter Plot of yearly CO2 emissions

#Scaling down the emissions value by multiplying by 0.00001, so i can reasonably
#plot the yearly emissions with the bubbles sized ("s=CO2_Emissions") per emissions value
CO2_Emissions_scaled=0.00001*(numpy.loadtxt('C:\\Users\Philip Abraham\OneDrive\TECHNOLOGY\Data Analysis\Data\CO2_Emissions2.txt', delimiter=',', unpack=True))

#Scatter plt with orange color and opacity("alpha")=.5
plt.scatter(year,emissions, s=CO2_Emissions_scaled,c='orange',alpha=.5,label='Loaded from file!')

# Additional customizations
plt.xlabel('Year')
plt.ylabel('CO2 Emissions')
plt.title('Yearly Global CO2 Emissions_1952-2008')
plt.legend()
plt.grid(True)
plt.text(1952,5568075, 'Relatively Small')
plt.text(2008,29675015, 'Relatively Large')

#Show Scatter Plot
plt.show()