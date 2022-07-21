w = 500
h = 500

class Team(object):
    global w,h
    def __init__(self, name_, x_, y_):
        self.name = name_
        self.x = x_
        self.y = y_
    
    def display(self):
        fill(128)
        textSize(32)
        text(self.name, self.x, self.y)
    
table1 = Team('sam', 30, 30)


def setup():
    global w, h
    size(w, h)
    background(32)
    
def draw():
    table1.display()
    
