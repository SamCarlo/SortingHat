import numpy as np
import pandas as pd

#First step is to upload the class data into this program. 
#No data cleanup is necessary, so this only requires one line of code.
X = pd.read_csv('roster.csv')

print(X['Name'])

n = []
for i in X:
    n.append(X['Name'])
n
        

#Second is to create new datasets that provide a roster sorted by students' subject scores. 
X_reading = X.sort_values('Reading Score')
X_science = X.sort_values('Science Score')
X_math = X.sort_values('Math Score')
X_grade = X.sort_values('Grade')
X_astronomy = X.sort_values('Astronomy score')
                           
astronomy_names = X_astronomy.iloc[:, [0]]
math_names = X_math.iloc[:,[0]]
science_names = X_science.iloc[:,[0]]
reading_names = X_reading.iloc[:,[0]]
grade_names = X_grade.iloc[:,[0]]

math_names.values

#Third step is to create table groups in the form of arrays. 
#I'll have to mutate the above pandas dataframes into numpy arrays. 
group_max = 5
count = 0 

math_names_np = math_names.to_numpy()
science_names_np = science_names.to_numpy()
astronomy_names_np = astronomy_names.to_numpy()
reading_names_np = reading_names.to_numpy()
grade_names_np = reading_names.to_numpy()

arr = []

def ranks(names):
    count = round(len(names)/3)
    for i in names:
        print(names[i])
        #if len(arr) == count:
           # return 0
        
    #return arr 
        
ranks(math_names_np)
        
        



    
    