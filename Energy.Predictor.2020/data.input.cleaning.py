# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:58:13 2020
Input of data
@author: dthoms
"""

import numpy as np
import pandas as pd

"""
Input Data
"""

"""
set up API to automatically date and download"
"""



#Input relevant files
bMetaData = pd.read_csv("kaggle-data/building_metadata.csv")
trainData = pd.read_csv("kaggle-data/train.csv")
trainWeatherData = pd.read_csv("kaggle-data/weather_train.csv")

#combine buildingMetaData and trainData
combDF = pd.merge(bMetaData,trainData,how='outer',on='building_id')


#trainWeatherData has irrelevant unused observations, remove observations
keys = list(['site_id','timestamp'])
i1 = trainWeatherData.set_index(keys).index
i2 = combDF.set_index(keys).index
trainWeatherData = trainWeatherData[i1.isin(i2)]

#combine combDF with revised trainWeatherData
combDF = pd.merge(combDF,trainWeatherData,how='outer',on=['site_id','timestamp'])

combDF.drop(columns = ['year_built','floor_count','cloud_coverage','precip_depth_1_hr'],
            inplace=True)

combDF.dropna(inplace = True)

#output csv
combDF.to_csv("data/combDF.csv", index = False)

#create samples
bMDSample = bMetaData.head(100)
trainSample = trainData.head(100)
weathTrainSample = trainWeatherData.head(100)
combDFSample = combDF.head(100)