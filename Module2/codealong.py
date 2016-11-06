# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:45:05 2016

@author: antuanweeks
"""

import pandas as pd

path = "/Users/antuanweeks/DAT210x/Module2/Datasets/direct_marketing.csv"

df = pd.read_csv(path)

df.head()

# Feature Representation

income_ordered = [
    '$1 - $1000',
    '$1000 - $10000',
    '$10000 - $100000',
    '$100000 - $1000000',
    '+$1000000']

df = pd.DataFrame({
    'income': [
        '$100000 - $1000000',
        '$10000 - $100000',
        '$1 - $1000',
        '+$1000000',
        '$1000 - $10000',
        '+$1000000',
        '+$1000000',
        '$10000 - $100000',
        '$10000 - $100000'
        ]
        })
        
print df

df.income = df.income.astype('category', 
                             ordered=True,
                             categories=income_ordered
                             ).cat.codes

print df

df = pd.DataFrame({'vertebrates': [
    'Bird', 
    'Mammal', 
    'Fish',
    ']})