# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:58:29 2020

@author: dthoms

Feature Engineering Iter 1 
- for machine lenrning do not need dummies for linear regression
"""

"""
MODULES
"""

import numpy as np
import pandas as pd
from data_cleaning_iter1_samp import df
import functions

"""
MAP METER VALUES
"""
#map values
meterName = {0: 'electricity', 1: 'chilledwater', 2: 'steam', 3: 'hotwater'}
df['meter'] = df['meter'].map(meterName)


"""
CREATE WIND DIRECTION VALUES
"""
df['wind_compass'] = df['wind_direction'].apply(lambda x:functions.wind_direction(x))
df.drop(['wind_direction'],axis=1,inplace=True)


"""
CONSOLIDATE PRIMARY USE
"""
#consolidate all but top 5 into other

y = ["Education","Office","Lodging/residential","Entertainment/public assembly",\
     "Public services","Healthcare","Other"]
df['primary_use'] = df['primary_use'].apply(lambda x: "Other" if x not in y else x  )

"""
CREATE CDD and HDD
"""
#assume CDD set point 24
#assume HDD set point 18

df['HDD'] = df['air_temperature'].apply(lambda x: functions.HDD(x))
df['CDD'] = df['air_temperature'].apply(lambda x: functions.CDD(x))

"""
OUTPUT NON-DUMMY VERSION
"""

df.to_csv("data/df_samp.csv", index = False)

"""
CREATE DUMMIES
"""

df = functions.create_dummy_drop_first(df,'meter')
df = functions.create_dummy_drop_first(df,'wind_compass')
df = functions.create_dummy_drop_first(df,'primary_use')
df = functions.create_dummy_drop_first(df,'hour')
df = functions.create_dummy_drop_first(df,'weekday')
df = functions.create_dummy_drop_first(df,'month')
df.info()

#create loop
#create dummy variables for hour, weekday, month
#drop building id, site id

df.to_csv("data/df_dummy_samp.csv", index = False)