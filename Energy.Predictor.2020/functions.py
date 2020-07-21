# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:34:50 2020

@author: dthoms
"""

'''
LIBRARIES
'''
import numpy as np
import pandas as pd
import gc

#remove building and meter data because not legitimate data
#set data as list
def remove_building_meter(file,bad_meters):
    #tuples make index shift by 1
    for row in bad_meters.itertuples():
        print(row[2])
        file.drop(file[(file['building_id'] == row[1]) & (file['meter'] == row[2])].index,inplace=True)
 
 
#create dummy variables
def create_dummy_drop_first(dataf,col):   
    dummy = pd.get_dummies(dataf[col],col,drop_first=True)
    dataf = pd.concat([dataf,dummy],axis=1)
    dataf.drop(col,axis=1,inplace=True)
    return dataf


#wind direction function
def wind_direction(x):
    if (x>=337.5) or (x <22.5):
        return "North"
    elif (x>=22.5) and (x <67.5):
        return "Northeast"
    elif (x>=67.5) and (x <112.5):
        return "East"
    elif (x>=112.5) and (x<157.5):
        return "Southeast"
    elif (x>=157.5) and (x<202.5):
        return "South"
    elif (x>=202.5) and (x<247.5):
        return "Southwest"
    elif (x>=247.5) and (x<292.5):
        return "West"
    else:
        return "Northwest"