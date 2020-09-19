# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:46:04 2020

@author: dthoms
"""

from zipfile import ZipFile

with ZipFile('kaggle-data/ashrae-energy-prediction.zip', 'r') as myzip:
    myzip.extractall('kaggle-data')