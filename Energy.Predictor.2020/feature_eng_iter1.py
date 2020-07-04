# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:58:29 2020

@author: dthoms

Feature Engineering Iter 1
"""

"""
MODULES
"""

import numpy as np
import pandas as pd


"""
CREATE DUMMY VALUES
"""
#map values
meterName = {0: 'electricity', 1: 'chilledwater', 2: 'steam', 3: 'hotwater'}
df['meter'] = df['meter'].map(meterName)
dummy = pd.get_dummies(df['meter'],drop_first=True)
df = pd.concat([df,dummy],axis=1)
df.drop(['meter'],axis=1,inplace=True)
