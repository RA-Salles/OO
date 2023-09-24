from . import drawer
from pointpack.pointhandlers import *
import numpy as np


class menu(erros):
    inp = None
    options = [
        '1. create a new figure',
        '2. print figures',
        '3. exit'
    ]
    funcs = [
        

    ]
    def printwelcome(self):
        print("WELCOME TO THE AMAZING PROGRAM!")
        print()
    def printoptions(self):
        
    def start(self):
        while self.inp != 'EXIT':
            self.getinput()
    def end(self):
        pass
    def getinput(self):
        self.inp = input()
    def createfigure(self):
        while self.inp != 'stop':
            print("input points for your figure! ex.: 42,37")
            print("input stop ")