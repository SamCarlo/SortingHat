size(1000, 1000)

n = 30
table_w = 150
table_h = 150

drop = 0
x = 0
y = 0

for i in range(n):
    rect(x+5, y+5, table_w, table_h) 
    drop += table_w
    x += table_w+5
    print(x, y)
    if drop >= 800:
        drop = 0
        x = 0
        y += table_h + 5
        
        
