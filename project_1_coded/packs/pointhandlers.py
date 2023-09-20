import numpy as np

class point():
    # this little guy will store like... everything for everyone.
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def getabsoluteval(self):
        return np.sqrt(x**2 + y**2)
    
    def update(self, x, y):
        self.x = x 
        self.y = y
        

class line():  # i actually shouldn't make this guy get any inheritance :> BECAUSE LINE CONTAINS MANY POINTS BUT ARE INHERENTLY DIFFERENT!!!!!!
    __errorflag = 0
    __message: str = "Undefined"
    points = []
    def __init__(self , list1: list , precision: int):
                #this should be a list of points
        self.__message = "Generating points"
        for item in list1:
            self.__message = "Checking list1 contents"
            if type(item) != point:
                print("Found non-point inside list1. Raised error flags")
                self.__errorflag = 1
            self.__message = "Checking precision type"
            if type(precision) != int:
                print("Precision not an integer. Raised error flags")
                self.__errorflag = 1
            if self.__errorflag == 0:
                print("Checks -> alright!\n\
                      moving on...")
        if self.__errorflag == 0: #meaning it was not raised
            self.limitpoints = list1 
            self.precision = precision
            self.makepoints() #already generates every point to make the line.
        else:
            self.errmessage()
        pass
    
    def makepoints(self): #this admits list1 and precision passed both tests
        """
            NOTE:
            Do not, for the love of almighty god,
            let this handle unordered lists. 
            The resulting figure will probably make
            you want to kys, which is suboptimal.
        """
        self.__message = "calculating average variation"
        m = (self.limitpoints[1].y - self.limitpoints[0].y)/(self.limitpoints[1].x - self.limitpoints[0].x)  #dy/dx = m
        self.__message = "adjusting point generator function"
        def f(x): #this function is generated in runtime. Meaning it is unique for every line. 
            y = m*(self.limitpoints[1].x-self.limitpoints[0].x) - self.limitpoints[1].y
            return y 
        self.__message = "calculating average variation"
        self.allx = np.linspace(self.limitpoints[0].x, self.limitpoints[1].x, self.precision) #this guy contains all x's for the entire line, which is made of points
        self.ally = [] #separating in lists of x's and y's will make it easier to use matplotlib.
        for x in self.allx:
            self.ally.append(f(x)) #if this works, then everything is quite fine!

        
                
            

        
    def precisiongetter():
        pass

    def errmessage(self):
        print("error detected in procedure", self.__message)
        print("memory liberated for object instance")
        pass

    def die(self):
        del self #this is a function to kill the object.
    pass


class figure():
    def __init__():
        pass

class circle(point):
    def __init__(x: float , y: float , radius: float , precision: int):
        pass
    