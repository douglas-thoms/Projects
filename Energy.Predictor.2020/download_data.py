# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:15:39 2020

Download files using API test

Source

https://stackoverflow.com/questions/55934733/documentation-for-kaggle-api-within-python

@author: dthoms
"""

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.competition_download_files('ashrae-energy-prediction', path='kaggle-data/')