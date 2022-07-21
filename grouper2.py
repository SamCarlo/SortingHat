import numpy as np
import pandas as pd

#First step is to upload the class data into this program. 
X = pd.read_csv('roster.csv')

#This works for printing out the sorted names

for i in X:
    n.append(X['Name'])
n

#function that sorts roster depending on which variable you choose
def sorting_hat():
    #sort by a subject score
    c = input('sort by which category? (Reading Score, Science Score, Math Score, Astronomy Score):')
    X_sorted = X.sort_values(c)
    n = X_sorted['Name']
    
    # group into 3 houses 
    cap = round(len(X)/3)
    g1 = n[[0,cap-1],:]
    g2 = n[[cap,-cap], :]
    g3 = n[-cap:, :]
    
    return g1, g2, g3
        
sorting_hat() 

   
   

   