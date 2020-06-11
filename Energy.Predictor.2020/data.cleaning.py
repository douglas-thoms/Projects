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




import numpy as np
import pandas as pd
import gc

combDF = pd.read_csv('data/combDF.csv')

bad_meters = pd.read_csv('data_cleaning/too_low_electricity_iter1.csv')

combDF.drop(columns = ['year_built','floor_count','cloud_coverage','precip_depth_1_hr'],
            inplace=True)

#removing Nan values (could use imputing for these rows instead)
combDF.dropna(inplace = True)

#list of buildings to remove
# combDF.drop(combDF[(combDF['building_id'] == 1099) & (combDF['meter'] == 2)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 778) & (combDF['meter'] == 1)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1021) & (combDF['meter'] == 3)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1168) & (combDF['meter'] == 2)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1197) & (combDF['meter'] == 2)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1148) & (combDF['meter'] == 2)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1159) & (combDF['meter'] == 2)].index,inplace=True)
# combDF.drop(combDF[(combDF['building_id'] == 1099) & (combDF['meter'] == 2)].index,inplace=True)   

#building_meter_remove = [[1099,2], [778,1], [1021,3],[1168,2],[1197,2],[1148,2],[1159,2],[1099,2]]
remove_building_meter(combDF, bad_meters)