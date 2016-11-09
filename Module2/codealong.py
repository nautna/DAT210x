# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:45:05 2016

@author: antuanweeks
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

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
    'Dog'
    ]
    })

# Pure textual features

corpus = ["""
Republican Donald Trump was rushed off stage by security agents at a rally in
Reno, Nevada, on Saturday night after a false alarm as someone in the crowd
shouted "gun" during scuffles with a man who held up a 'Republicans against
Trump' sign.""", """

The incident occurred as Trump and Democratic rival Hillary Clinton
 crisscrossed the United States a late push to win over undecided voters and
 make sure supporters turn out enthusiastically on Election Day.""", """

Two security agents seized Trump by the shoulders and hustled him backstage as
police officers swarmed over a man in the front of the crowd and held him down
and searched him before escorting him away with his hands behind his back."""]

bow = CountVectorizer(ngram_range=(4, 5))
X = bow.fit_transform(corpus) # soarse matrix

print bow.get_feature_names()

X.toarray()