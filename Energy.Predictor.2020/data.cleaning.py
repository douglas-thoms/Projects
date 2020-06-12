# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:04:17 2020

@author: dthoms
"""

#FUNCTIONS
#remove building and meter data because not legitimate data
#set data as list

def remove_building_meter(file,bad_meters):
    #tuples make index shift by 1
    for row in bad_meters.itertuples():
        print(row[2])
        file.drop(file[(file['building_id'] == row[1]) & (file['meter'] == row[2])].index,inplace=True)
    #  for entry in list:
   #     file.drop(file[(file['building_id'] == entry[0]) & (file['meter'] == entry[1])].index,inplace=True)


#create method combining all elimination dataframe



import numpy as np
import pandas as pd
import gc

combDF = pd.read_csv('data/combDF.csv')

too_low_electricity = pd.read_csv('data_cleaning/too_low_electricity_iter1.csv')
general_outlier = pd.read_csv('data_cleaning/general_outlier_iter1.csv')
too_low_chilledwater = pd.read_csv('data_cleaning/too_low_chilledwater_iter1.csv')

bad_meters = pd.merge(too_low_electricity, general_outlier, how='outer')
bad_meters = pd.merge(bad_meters, too_low_chilledwater, how='outer')

combDF.drop(columns = ['year_built','floor_count','cloud_coverage','precip_depth_1_hr'],
            inplace=True)

#removing Nan values (could use imputing for these rows instead)
combDF.dropna(inplace = True)

remove_building_meter(combDF, bad_meters)