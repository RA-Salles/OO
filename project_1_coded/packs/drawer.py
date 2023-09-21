import matplotlib.pyplot as plot
from pointpack.pointhandlers import errors
def test1(): #proof that scatter works alrighty alright!
    x = [1,2,3]
    y = [1,2,3]
    plot.scatter(x, y)
    plot.show()

class drawer(errors):
    def __init__(self, figurelist: list):
        self.figurelist = figurelist
        self.gatherpoints()
        self.show()
    def gatherpoints(self):
        self.allx = []
        self.ally = []
        for figure in self.figurelist:
            for x in figure.allx:
                self.allx.append(x)
            for y in figure.ally:
                self.ally.append(y)
    def show(self): #as easy as that
        plot.scatter(self.allx, self.ally)
        plot.show()

        
