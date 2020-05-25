# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:30:09 2020

@author: dthoms
"""

import numpy as np
import pandas as pd
import gc

trainData = pd.read_csv('kaggle-data/train.csv')
trainData['timestamp'] = pd.to_datetime(trainData.timestamp)

trainWeatherData = pd.read_csv("kaggle-data/weather_train.csv")
trainWeatherData['timestamp'] = pd.to_datetime(trainWeatherData.timestamp)
trainWeatherData['hour'] = trainWeatherData.timestamp.dt.hour
trainWeatherData['weekday'] = trainWeatherData.timestamp.dt.dayofweek
trainWeatherData['month'] = trainWeatherData.timestamp.dt.month

bMetaData = pd.read_csv("kaggle-data/building_metadata.csv")

combDF = pd.merge(bMetaData,trainData,how='inner',on='building_id')

del trainData
gc.collect()

combDF = pd.merge(combDF,trainWeatherData,how='inner',on=['site_id','timestamp'])
combDF.info()

#output csv
combDF.to_csv("data/combDF.csv", index = False)