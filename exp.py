#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:38:30 2022

@author: user
"""

#experimenting with pandas.. trying to add new columns
import pandas as pd
df = pd.read_csv('/Users/user/Documents/Processing/table_drawer/roster.csv')
df

#a teller of rank to create a variable to assign

df_high = df[df['Math Score'] > 70]
df_low = df[df['Math Score'] < 40]

#Returns the section of the dataframe whose maths are > 70
df[df['Math Score'] > 70]

#Creates a new column of all 1's
df2 = df.assign(math_rank = 1)

#turns the dataframe into a numpy array
arr = df.to_numpy()

#prints every row as an element, but is agnostic to columns
for i in arr:
    print (i) 

#sorts the dataframe by math score
df_math = df.sort_values('Math Score')

#creates a dataframe of only the names & math scores. Automating requires dictionary. 
df_math = df.iloc[:, [0,3]]

df_astro = df.iloc[:,[0,5]]

#add a column to df_astro
df_astro_rank = df_astro.assign(astro_rank = 1)

#function to determine if astro score is high or low
#put rank back into assign function? 
scores = df_astro_rank['Astronomy score']
rank = []
for i in scores:
    if i > 60:
        rank.append('High')
    if 60 > i > 50:
        rank.append('Med')
    if 50 > i > 0:
        rank.append('Low')
rank

#put ranks into a df
ranked_astro = df_astro.assign(Rank = rank)

#return groups by rank
high_astro = ranked_astro[ranked_astro['Rank'] == 'High']
med_astro = ranked_astro[ranked_astro['Rank'] == 'Med']
low_astro = ranked_astro[ranked_astro['Rank'] == 'Low']

#sorting hat function: create groups that spread astro skill around among the groups
#I want to sort into even groups for this:
sorted_scores_ = df_astro_rank.sort_values('Astronomy score')
sorted_scores = sorted_scores_.iloc[:,1]
groups = []
for i in sorted_scores:
    #why doesn't this work?
    print(sorted_scores[i])
    
#What if I just made a random sorter? 
#shuffle method randomizes the order of a list
sorted_scores_.shuffle()
#but that only works on lists, so...

#how about the .sample method?
#***THIS is what i needed
#see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html
df_shuffled0 = df['Name'].sample(frac=1, replace = False, random_state=1)

#create many individual samples
#random_state acts as a "seed" for a pseudo-random number generator. 
df_shuffled1 = df['Name'].sample(n=5, replace = False)
df_shuffled2 = df['Name'].sample(n=5, replace = False)
df_shuffled3 = df['Name'].sample(n=5, replace = False)
df_shuffled4 = df['Name'].sample(n=5, replace = False)
df_shuffled5 = df['Name'].sample(n=3, replace = False)
df_shuffled6 = df['Name'].sample(n=3, replace = False)

#attach them all together
#Not quite what I wanted, it just lists them all. I need separate cols. 
frames = [df_shuffled1, df_shuffled2, df_shuffled3, df_shuffled4, df_shuffled5, df_shuffled6]
grouped = pd.concat(frames, axis = 1, ignore_index=True)

#another approach: just randomy sort the class and then cut into groups
df_shuffled0 = df['Name'].sample(frac=1, replace = False, random_state=1)
for row in df_shuffled0:
    print(row)

#append some to new list
group1 = df_shuffled0.iloc[0:5]
group2 = df_shuffled0.iloc[5:10]
group3 = df_shuffled0.iloc[10:15]
group4 = df_shuffled0.iloc[15:20]
group5 = df_shuffled0.iloc[20:23]
group6 = df_shuffled0.iloc[23:]


#stitch together
grps_ = [group1["Name"], group2["Name"], group3["Name"], group4["Name"], group5["Name"], group6["Name"]]
grouped = pd.concat(grps_, axis = 1, ignore_index = True)
#doesn't make sense for my purposes really.
    


#then use groupby to sort into groups? 
#https://realpython.com/pandas-groupby/






