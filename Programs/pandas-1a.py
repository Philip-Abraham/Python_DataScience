# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:59:33 2016

@author: JJALAW
"""

import pandas as pd

import os
os.getcwd() # Returns the current working directory; usually the directory you were in when you started the interpreter

# Change the current working directory to 'path/to/directory'. Also accepts bash commands like '..' and '/'
os.chdir('C:/Users/Philip Abraham/OneDrive/TECHNOLOGY/Data Analysis/Data/Meteorological/US Cities Precipitation Data/Los Angeles Intl Arpt/') 
os.getcwd() # Returns the current working directory; usually the directory you were in when you started the interpreter

#Bring in the CSV file from the current working directory
LAJanData = pd.read_csv("LA_Precip-Jan.csv",index_col=0)

#Show all the Year(1945-2015) January climate data
print(LAJanData)

#Show all the Year(1945-2015) January Precip data
JanPrecip=LAJanData["TotalPrecip"]
print(JanPrecip)

#Show Year 2012 precip ROW data
print(LAJanData.loc["Y2012"])

#Print as Series the Year 2012 precip data
print(LAJanData.loc["Y2012","TotalPrecip"])

# Print sub-DataFrame of precipitation in Years 1983 and 1997
print(LAJanData.loc[['Y1983','Y1997'],['MeanT','TotalPrecip']])

#PLOTTING
import matplotlib.pyplot as plt
#Customized Scatter Plot of yearly LA Precip from 1945 to 2015

#Show all the Year(1945-2015) January  mean temperature data
Mean_Temp=LAJanData["MeanT"]
print(Mean_Temp)

#Show all the Year(1945-2015) January scaled deviation from mean temperature data
dev_Temp=100*LAJanData["dev"]
print(dev_Temp)

Year=LAJanData["Year"]
#Scatter plt with blue color and opacity("alpha")=.8
plt.scatter(Year,JanPrecip,s=dev_Temp,c='blue',alpha=.8)

# Additional customizations
plt.xlabel('Year')
plt.ylabel('Jan Precip')
plt.title('Los Angeles January Precipitation_1945-2012')

plt.grid(True)


#Show Scatter Plot
plt.show()

#Show plot of Jan precip versus Jan mean Temp
plt.scatter(Mean_Temp,JanPrecip,c='green',alpha=.8)
plt.xlabel('Jan Mean Temp')
plt.ylabel('Jan Precip')
plt.title('Los Angeles Mean Temp vs. January Precipitation_1945-2012')
plt.grid(True)
plt.show()



