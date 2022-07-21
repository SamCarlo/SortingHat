#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:01:48 2022

@author: user
"""

import pandas as pd

roster = pd.read_csv('roster.csv')

def ranker():
    global roster
    c = input('rank which category? (Reading Score, Science Score, Math Score, Astronomy Score):')
    X_ranked = X.sort_values(c)
    return(roster[c])
    

d = ranker()

def sorting_hat(scores):
    
    for row in scores:
            if row <= 30:
                scores.loc[:,('rank')] = 0
            if 30 < row <= 70:
                scores.loc[:,('rank')] = 1
            if row > 70:
                sscores.loc[:,('rank')] = 2
            else:
                return scores
            
    return scores
       
sorting_hat(d)


     
            