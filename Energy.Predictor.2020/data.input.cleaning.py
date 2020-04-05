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




buildingMetaData = pd.read_csv("kaggle-data/building_metadata.csv")
trainData = pd.read_csv("kaggle-data/train.csv")
trainWeatherData = pd.read_csv("kaggle-data/weather_train.csv")

bMDSample = buildingMetaData.head(100)
trainSample = trainData.head(100)
weathTrainSample = trainWeatherData.head(100)

test = pd.merge(trainData,buildingMetaData,how='outer',on='building_id')

test = pd.merge(test,trainWeatherData,how='outer',on='site_id')
testSample = test.head(100)

print(buildingMetaData)

#Study spider reports and pweave