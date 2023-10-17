from . import drawer
from pointpack.pointhandlers import *
import numpy as np
from .utils import numberparse as parser


class menu(errors):
    inp = None
    options = [
        'cfig',
        'ccir',
        'printfigs',
        'exit'
    ]
    precision = 20  # this is the global precision. Changing it requires overwriting in runtime before starting

    def start(self):
        self.figs = []
        self.printwelcome()
        self.printopt()

    def printopt(self):
        print("these are the commands:")
        for opt in self.options:
            print(opt)
        self.deffuncs()  # prepares the self.funcs
        while True:
            self.getinput()
            try:
                self.funcs[self.inp]()  # tries to call function passed
            except:
                # if function does not exist, gives out a command not found!
                print("command not found!")

    def printwelcome(self):
        print("WELCOME TO THE AMAZING PROGRAM!")
        self.printopt()

    def exit(self):
        """this guy handles exiting in a more cohesive way"""
        print("thanks for using the program!")
        quit()

    def getinput(self):
        self.inp = input()

    def createfigure(self):
        print("input points for your figure! ex.: 42,37 (x, y)")
        print("input stop to stop giving points!")
        points = []
        while self.inp != 'stop':
            self.getinput()
            # parser will only handle two points always. If more points are passed, they're ignored!
            z = parser(self.inp)
            if z == 'error' or len(z) < 2:
                print("point invalid! fix it in the next point.")
            else:
                points.append(point(float(z[0]), float(z[1])))
        print("input a center point. ex.: 42,49 ")
        self.getinput()
        z = parser(self.inp)
        try:
            center = [float(z[0]), float(z[1])]
        except:
            print("funnee!")
            error = 1
        if error == 0:
            print("saving figure!")
        self.figs.append(points, center, self.precision)

    def createcircle(self):
        print("input a center point for your circle. ex.: 23, -90")
        self.getinput()
        # will return as string in the format [x, y]. Make sure to float it.
        center = parser(self.inp)

    def printfigs(self):  # this guy gotta create a drawer and pass in the figure list
        self.handler = drawer()
        drawer(self.figs)
        pass

    def deffuncs(self):  # create a dict for the functions in options which resides inside the class
        self.funcs = {
            'cfig': self.createfigure,
            'ccir': self.createcircle,
            'printfigs': self.printfigs,
            'exit': self.exit
        }
