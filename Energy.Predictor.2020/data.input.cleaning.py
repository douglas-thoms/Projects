# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:58:13 2020
Input of data
@author: dthoms
"""

import numpy as np
import pandas as pd
import dask.dataframe as dd


"""
Input Data
"""

"""
set up API to automatically date and download"
"""

#set up dask
from dask.distributed import Client
client = Client(n_workers=4)




#Input relevant files
bMetaData = dd.read_csv("kaggle-data/building_metadata.csv")
trainData = dd.read_csv("kaggle-data/train.csv")
trainWeatherData = dd.read_csv("kaggle-data/weather_train.csv")

#remove outlier


#breakdown timestamp
trainData['timestamp'] = dd.to_datetime(trainData.timestamp)
trainWeatherData['timestamp'] = dd.to_datetime(trainWeatherData.timestamp)
trainWeatherData['hour'] = trainWeatherData.timestamp.dt.hour
trainWeatherData['weekday'] = trainWeatherData.timestamp.dt.dayofweek
trainWeatherData['month'] = trainWeatherData.timestamp.dt.month

#REMOVE DMAPPING HERE MOVE TO EDA
#dmap metering points, day of week
#weekdayName = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
#trainWeatherData['weekday'] = trainWeatherData['weekday'].map(weekdayName)
#monthName = {1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
#trainWeatherData['month'] = trainWeatherData['month'].map(monthName)
#meterName = {0: 'electricity', 1: 'chilledwater', 2: 'steam', 3: 'hotwater'}
#trainData['meter'] = trainData['meter'].map(meterName)

#combine buildingMetaData and trainData
combDF = pd.merge(bMetaData,trainData,how='inner',on='building_id')

#combine combDF with revised trainWeatherData
combDF = pd.merge(combDF,trainWeatherData,how='inner',on=['site_id','timestamp'])

combDF.drop(columns = ['year_built','floor_count','cloud_coverage'],
            inplace=True)

combDF.dropna(inplace = True)

#NEED FUNCTION
#remove following meters because of bad data
combDF.drop(combDF[(combDF['building_id'] == 1099) & (combDF['meter'] == 2)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 778) & (combDF['meter'] == 1)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1021) & (combDF['meter'] == 3)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1168) & (combDF['meter'] == 2)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1197) & (combDF['meter'] == 2)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1148) & (combDF['meter'] == 2)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1159) & (combDF['meter'] == 2)].index,inplace=True)
combDF.drop(combDF[(combDF['building_id'] == 1099) & (combDF['meter'] == 2)].index,inplace=True)

combDF = combDF[['timestamp','hour','weekday','month', 'site_id', 'building_id', 'meter', 'meter_reading', 'primary_use', 'square_feet', 'air_temperature', 'dew_temperature', 'sea_level_pressure', 'wind_direction', 'wind_speed']]


#output csv
combDF.to_csv("data/combDF.csv", index = False)
# trainWeatherData.to_csv("data/trainWeatherData.csv", index = False)
# trainData.to_csv("data/trainData.csv", index = False)
# bMetaData.to_csv("data/bMetaData.csv", index = False)

#create samples
bMDSample = bMetaData.head(100)
trainSample = trainData.head(100)
weathTrainSample = trainWeatherData.head(100)
combDFSample = combDF.head(100)

