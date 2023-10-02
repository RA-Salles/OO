from . import drawer
from pointpack.pointhandlers import *
import numpy as np
from .utils import numberparse as parser


class menu(erros):
    inp = None
    options = [
        'cfig',
        'ccir',
        'printfigs',
        'exit'
    ]

    def printopt(self):
        print("these are the commands:")
        for opt in self.options:
            print(opt)
        self.deffuncs()

    def printwelcome(self):
        print("WELCOME TO THE AMAZING PROGRAM!")
        self.printopt()

    def start(self):
        while self.inp != 'exit':
            self.getinput()
        else:
            self.exit()

    def exit(self):
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
            z = parser(self.inp)
            if z == 'error' or len(z) < 2:
                print("point invalid! fix it in the next point.")
            else:
                points.append(point(str(z[0]), str(z[1])))

    def createcircle(self):
        print("input a center point for your circle")
        self.getinput()
        center = parser(self.inp)

    def printfigs(self):  # this guy gotta create a drawer and pass in the figure list
        pass

    def deffuncs(self):  # create a dict for the functions in options which resides inside the class
        self.funcs = {
            'cfig': self.createfigure,
            'ccir': self.createcircle,
            'printfigs': self.printfigs,
            'exit': self.exit
        }
