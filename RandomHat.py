

import pandas as pd

#Step 1: import a class roster
df = pd.read_csv('roster.csv')

#Step 2: shuffle the class roster randomly
df_shuffled0 = df['Name'].sample(frac=1, replace = False)

#Step 3: display groups of size z from the list
z = int(input("how many students per group?"))
n = 0
table = []
for i in df_shuffled0:
    table.append(i)
    n += 1
    if n >= z:
        #print every time you fill a group of 4
        print(table)
        print('______________')
        table = []
        #return back to 'for' loop
        n = 0
#print the remainder group
print(table)


#######
