import numpy as np

class errors():
    """
        errors is a collection of utils for error handling. 
        basically, the class should generate a log of everything it did.
        if it fails, meaning it raised the __errorflag, it dumps the log
        and quits.
    """
    errorflag = 0
    message: list = [] #this is a collection of logs from the running of the function. If it detects an error through error flag, it log dumps and stops.
    def error(self):
        for message in self.message:
            print(message) #meaning it log dumps
        print("erratic behaviour averted!")
        print("quitting...")
        quit() #it is a very angry program :>

    def die(self):
        del self #this is a function to kill the object.


class point(errors):
    # this little guy will store like... everything for everyone.
    def __init__(self, x: float, y: float):
        self.message.append("managing ")
        self.x = x
        self.y = y
    
    def getabsoluteval(self):
        return np.sqrt(x**2 + y**2)
    
    def update(self, x, y):
        self.x = x 
        self.y = y
        

class line(errors):  # i actually shouldn't make this guy get any inheritance :> BECAUSE LINE CONTAINS MANY POINTS BUT ARE INHERENTLY DIFFERENT!!!!!!
    points = []
    def __init__(self , list1: list , precision: int):
                #this should be a list of points
        self.message.append("Generating points")
        for item in list1:
            self.message.append("Checking list1 contents")
            if type(item) != point:
                self.message.append("Found non-point inside list1. Raised error flags")
                self.errorflag = 1
            self.message.append("Checking precision type")
            if type(precision) != int:
                self.message.append("Precision not an integer. Raised error flags")
                self.errorflag = 1
            if self.errorflag == 0:
                self.message.append("Checks -> alright!\n\
                                      moving on...")
        if self.errorflag == 0: #meaning it was not raised and all is fine.
            self.limitpoints = list1 
            self.precision = precision
            self.makepoints() #already generates every point to make the line.
        else:
            self.error()
        pass
    
    def makepoints(self, **kwargs): #this admits list1 and precision passed both tests
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
        f =lambda x: m*(self.limitpoints[1].x-self.limitpoints[0].x) - self.limitpoints[1].y  #this function is generated in runtime. Meaning it is unique for every line.
        self.__message = "calculating average variation"
        self.allx = np.linspace(self.limitpoints[0].x, self.limitpoints[1].x, self.precision) #this guy contains all x's for the entire line, which is made of points
        self.ally = [] #separating in lists of x's and y's will make it easier to use matplotlib.
        for x in self.allx:
            self.ally.append(f(x)) #if this works, then everything is quite fine!
        
        if 'debug' in kwargs:
            print(self.allx)
            print(self.ally)


class figure(errors):
    def __init__():
        pass
    def linemaker():
        pass
    

class circle(point, errors):
    def __init__(self , x: float , y: float , radius: float , precision: int):
        """
        a circle got a center and a radius, which is great
        """
        self.message.append("checking variables")
        if type(radius) != float:
            self.message.append("radius is not float or float compatible. Trying to fix")
            try:
                radius = float(radius)
            except:
                self.message.append("unable to fix radius, errorflag raised")
                self.errorflag = 1

        if type(precision) != int:
            self.message.append("precision is not int or int compatible. Trying to fix")
            try:
                precision = int(precision)
            except:
                self.message.append("unable to fix precision, errorflag raised")
                self.errorflag = 1
        super.__init__()
        if self.errorflag == 1:
            self.error()
        else:
            self.message.append("variable initialization success. Processing lines!")
     