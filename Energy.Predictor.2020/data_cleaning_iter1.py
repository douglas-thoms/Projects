# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:04:17 2020

@author: dthoms

Iteration 1
-found meter-ids with unusually high values
-searched for low and unusual values in electricity, steam, chilled water, hot water
-removed spikes
-no imputation in weather or building id, just removed empty rows or full columns

"""

'''
LIBRARIES
'''
import numpy as np
import pandas as pd
import gc
import functions

'''
INPUT FILES
'''

trainData = pd.read_csv('kaggle-data/train.csv')
trainData['timestamp'] = pd.to_datetime(trainData.timestamp)

trainWeatherData = pd.read_csv("kaggle-data/weather_train.csv")
trainWeatherData['timestamp'] = pd.to_datetime(trainWeatherData.timestamp)
trainWeatherData['hour'] = trainWeatherData.timestamp.dt.hour
trainWeatherData['weekday'] = trainWeatherData.timestamp.dt.dayofweek
trainWeatherData['month'] = trainWeatherData.timestamp.dt.month

bMetaData = pd.read_csv("kaggle-data/building_metadata.csv")

too_low_electricity = pd.read_csv('data_cleaning/too_low_electricity_iter1.csv')
general_outlier = pd.read_csv('data_cleaning/general_outlier_iter1.csv')
too_low_chilledwater = pd.read_csv('data_cleaning/too_low_chilledwater_iter1.csv')
too_low_hotwater = pd.read_csv('data_cleaning/too_low_hotwater_iter1.csv')

rolling_average = pd.read_csv("kaggle-data/train.csv")

'''
DATA CLEANING
'''

#remove incomplete columns
trainWeatherData.drop(columns = ['cloud_coverage','precip_depth_1_hr'],
            inplace=True)

bad_meters = pd.merge(too_low_electricity, general_outlier, how='outer')
bad_meters = pd.merge(bad_meters, too_low_chilledwater, how='outer')
bad_meters = pd.merge(bad_meters, too_low_hotwater, how='outer')

bMetaData.drop(columns = ['year_built','floor_count'],
            inplace=True)

functions.remove_building_meter(trainData, bad_meters)


#Create rolling average to remove spike
rolling_average['meter_reading_roll_avg'] = rolling_average['meter_reading']
rolling_average.set_index('timestamp',inplace=True)

rolling_average = rolling_average[['building_id','meter','meter_reading_roll_avg']]\
    .groupby(['building_id','meter']).rolling(101,center=True,min_periods=1).mean()

rolling_average.drop(columns=['building_id','meter'], inplace=True)

rolling_average.reset_index(inplace = True)
rolling_average['timestamp'] = pd.to_datetime(rolling_average.timestamp)

trainData = pd.merge(trainData,rolling_average, on=['building_id','meter','timestamp'], how='inner')

#del rolling_average
#gc.collect()

trainData['outlier_ratio'] = trainData['meter_reading'] / trainData['meter_reading_roll_avg']

trainData = trainData[(trainData['outlier_ratio'] < 3) | (trainData['outlier_ratio'].isnull())]



#merge tables
df = pd.merge(bMetaData,trainData,how='inner',on='building_id')

#del trainData
#gc.collect()

df = pd.merge(df,trainWeatherData,how='inner',on=['site_id','timestamp'])
df.info()

#removing Nan values (could use imputing for these rows instead)
df.dropna(inplace = True)

#df.to_csv("data/df.csv", index = False)
