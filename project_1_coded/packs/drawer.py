import matplotlib.pyplot as plot
from pointpack.pointhandlers import *


def test1():  # proof that scatter works alrighty alright!
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot.scatter(x, y)
    plot.show()


class drawer(errors):
    def __init__(self, figurelist: list, **kwargs):
        self.figurelist = figurelist
        self.message.append("Checking figure list")
        for fig in self.figurelist:
            if type(fig) != figure:
                self.message.append("object in figure list not figure")
                self.message.append("raised error flags")
                self.errorflag == 1
        if self.errorflag == 1:
            self.error
        else:
            self.gatherpoints()
            if kwargs['instashow'] == 1:
                self.show

    def gatherpoints(self):
        self.allx = []
        self.ally = []
        for figure in self.figurelist:
            for x in figure.allx:
                self.allx.append(x)
            for y in figure.ally:
                self.ally.append(y)

    def show(self):  # as easy as that
        plot.scatter(self.allx, self.ally)
        plot.show()
