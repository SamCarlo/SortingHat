#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 16:45:03 2022

@author: user
"""

import pandas as pd

#Step 1: import a class roster
df = pd.read_csv('roster.csv')

#Step 2: shuffle the class roster randomly
df_shuffled0 = df['Name'].sample(frac=1, replace = False)

#Step 3: append some to new list
group1 = df_shuffled0.iloc[0:4]
group2 = df_shuffled0.iloc[4:8]
group3 = df_shuffled0.iloc[8:12]
group4 = df_shuffled0.iloc[12:16]
group5 = df_shuffled0.iloc[16:20]
group6 = df_shuffled0.iloc[20:24]
group7 = df_shuffled0.iloc[23:]

#Step 4: bring them all together into a new dataframe
group1 = group1.reset_index()
group2 = group2.reset_index()
group3 = group3.reset_index()
group4 = group4.reset_index()
group5 = group5.reset_index()
group6 = group6.reset_index()
group7 = group7.reset_index()

grps_ = [group1["Name"], group2["Name"], group3["Name"], group4["Name"], group5["Name"], group6["Name"], group7["Name"]]
grouped = pd.concat(grps_, axis = 1, ignore_index = True)

print(grouped)
