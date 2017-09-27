# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 08:42:34 2016

@author: JJALAW
"""
import os
os.getcwd() # Returns the current working directory; usually the directory you were in when you started the interpreter

# Change the current working directory to 'path/to/directory'. Also accepts bash commands like '..' and '/'
os.chdir('C:/Users/Philip Abraham/OneDrive/TECHNOLOGY/Data Analysis/Data/Meteorological/US Cities Precipitation Data/Los Angeles Intl Arpt/') 
os.getcwd() # Returns the current working directory; usually the directory you were in when you started the interpreter

#Bring in a CSV file from the current working directory
LAJanData = pd.read_csv("LA_Precip-Jan.csv")