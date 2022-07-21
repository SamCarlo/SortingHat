import pandas as pd

#Step 1: import a class roster
df = pd.read_csv('roster.csv')

#Step 2: sort the roster according to a defined score
c = input('sort by which category? (Reading Score, Science Score, Math Score, Astronomy Score):')
df_sorted_ = df.sort_values(c)

#step 3: peel off only the names of that sorting
df_sorted = df_sorted_['Name']

#Step 4: display groups of size z, grouped by their chosen subject score
z = int(input("how many students per group?"))
n = 0
table = []
for i in df_sorted:
    table.append(i)
    n += 1
    if n >= z:
        #print every time you fill a group of 4
        print(table)
        print('______________')
        table = []
        #return back to 'for' loop
        n = 0
#print the remainder table
print(table)
