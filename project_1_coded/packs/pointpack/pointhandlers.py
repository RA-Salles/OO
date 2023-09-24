"""
    Made by B@dC0d&L0cvst! during 2023.2. 
    Violent thoughts are very fun!
    But try to keep a low profile :>
"""

import numpy as np


class errors():
    """
        errors is a collection of utils for error handling. 
        basically, the class should generate a log of everything it did.
        if it fails, meaning it raised the __errorflag, it dumps the log
        and quits.
    """
    errorflag: int = 0
    # this is a collection of logs from the running of the function. If it detects an error through error flag, it log dumps and stops.
    message: list = []

    def error(self):
        for message in self.message:
            print(message)  # meaning it log dumps
        print("erratic behaviour averted!")
        print("quitting...")
        quit()  # it is a very angry program :>

    def die(self):
        del self  # this is a function to kill the object.


class point(errors):
    # this little guy will store like... everything for everyone.
    def __init__(self, x: float, y: float):
        # this guarantees errorflag will start as 0 - not raised.
        self.errorflag = 0
        self.message.append("realizing checks")
        if type(x) != float:
            self.message.append("x not float. Trying to fix")
            try:
                x = float(x)
            except:
                self.message.append("unable to fix x. Raising error flag")
            self.errorflag = 1
        if type(y) != float:
            self.message.append("y not float. Trying to fix")
            try:
                y = float(x)
            except:
                self.message.append("unable to fix y. Raising error flag")
            self.errorflag = 1
        if self.errorflag == 1:
            self.error()
        else:
            self.x = x
            self.y = y

    # returns the numerical distance to the origin. Might be useful somehow later.
    def getmod(self):
        return np.sqrt(self.x**2 + self.y**2)

    def update(self, x, y):
        self.x = x
        self.y = y


class line(errors):  # Everybody should inherit errors. Else it will get funny.
    points = []

    # list 1 should be a list containing no more, no less than 2 points. If there are more, points after position 1 will be ignored.
    def __init__(self, list1: list, precision: int):
        self.message.append("Generating points")
        for item in list1:
            self.message.append("Checking list1 contents")
            if type(item) != point:
                self.message.append(
                    "Found non-point inside list1. Raised error flags")
                self.errorflag = 1
            self.message.append("Checking precision type")
            if type(precision) != int:
                self.message.append(
                    "Precision not an integer. Raised error flags")
                self.errorflag = 1
            if self.errorflag == 0:
                self.message.append("Checks -> alright!\n\
                                      moving on...")
        if self.errorflag == 0:  # meaning it was not raised and all is fine.
            self.limitpoints = list1
            self.precision = precision
            # already generates every point to make the line.
            self.makepoints()
            # self.limitpoints = None #cleans it to use less memory. I guess. Decided to comment it so getsize will function easier.
        else:
            self.error()
        pass

    def makepoints(self, **kwargs):  # this admits list1 and precision passed both tests
        """
            NOTE:
            Do not, for the love of almighty god,
            let this handle unordered lists. 
            The resulting figure will probably make
            you want to kys, which is suboptimal.
        """
        self.__message = "calculating average variation"
        m = (self.limitpoints[1].y - self.limitpoints[0].y) / \
            (self.limitpoints[1].x - self.limitpoints[0].x)  # dy/dx = m
        self.__message = "adjusting point generator function"
        # this function is generated in runtime. Meaning it is unique for every line.

        def f(x): return m * \
            (self.limitpoints[1].x-self.limitpoints[0].x) - \
            self.limitpoints[1].y
        self.__message = "calculating average variation"
        # this guy contains all x's for the entire line, which is made of points
        self.allx = np.linspace(
            self.limitpoints[0].x, self.limitpoints[1].x, self.precision)
        # separating in lists of x's and y's will make it easier to use matplotlib.
        self.ally = []
        for x in self.allx:
            # if this works, then everything is quite fine!
            self.ally.append(f(x))

        if 'debug' in kwargs:
            print(self.allx)
            print(self.ally)

    def getsize(self):  # this guy will always run after init, so we gotta use
        # basic arithmetic is very good once in a while.
        return np.sqrt((self.limitpoints[1].x - self.limitpoints[0].x)**2 + (self.limitpoints[1].y - self.limitpoints[0].y)**2)


class figure(errors):
    """
        is always closed. To make an 'open figure', you should use line collection.
    """

    # the pointlist should be a list of point classes.
    def __init__(self, pointlist: list, center, precision: int):
        self.message.append("checking pointlist")
        i = -1
        for p in pointlist:
            i += 1
            if type(p) != point:
                self.message.append("object in position", i,
                                    "not point. Raising errorflag")
                self.errorflag = 1
        if center != point:
            self.message.append("Center not point. Trying to fix")
            try:
                # meaning it was passed as a [float, float], which is acceptable
                center = point(center[0], center[1])
            except:
                self.message.append("Unable to fix. errorflag raised")
                self.errorflag = 1
        if precision != point:
            self.message.append("preicision not integer. errorflag raised")
            self.errorflag = 1
        if self.errorflag == 1:  # meaning it was raised
            self.error()
        else:
            self.message.append(
                "Checks alright! Saving vars and making lines!")
            self.pointlist = pointlist
            self.center = center
            self.precision = precision
            self.makelines()

    def makelines(self):
        """
        this guy is very very crude and will not even try 
        to check anything. Make sure to use him only after
        checking the stuff.
        """
        self.linelist = []
        self.allx = []
        self.ally = []
        for i in range(len(self.pointlist)):  # this will run for every point
            if i == (len(self.pointlist) - 1):
                # this guy chains point with point to construct the lines
                self.linelist.append(
                    line(self.pointlist[i], self.pointlist[i+1]))
            else:
                # and this handles the last point, which should be chained to the first
                self.linelist.append(
                    line(self.pointlist[i], self.pointlist[0]))
        for l in self.linelist:
            pass


class circle(point):
    def __init__(self, x: float, y: float, radius: float, precision: int):
        """
        a circle got a center and a radius, which is great.
        To translate the circle to its center, we basically 
        must sum every x to its centerx and every y to its 
        center y. 
        Basically:
            radius -> duh
            precision -> defines the number of points which your circle will get to draw its form
            x and y -> defines the center.
        """
        self.message.append("checking variables")
        if type(radius) != float:
            self.message.append(
                "radius is not float or float compatible. Trying to fix")
            try:
                radius = float(radius)
            except:
                self.message.append("unable to fix radius, errorflag raised")
                self.errorflag = 1

        if type(precision) != int:
            self.message.append(
                "precision is not int or int compatible. Trying to fix")
            try:
                precision = int(precision)
            except:
                self.message.append(
                    "unable to fix precision, errorflag raised")
                self.errorflag = 1
        # this guy should already go ahead and test the x and y.
        super().__init__(x, y)
        # only trouble might come when it finds an error, but this is user skill issue

        if self.errorflag == 1:  # meaning it was raised.
            self.error()
        else:
            self.message.append(
                "variable checking success. Saving and generating points!")
            self.radius = radius
            self.precision = precision
            self.x = x
            self.y = y

    def pointgetter(self):
        """
            this guy should be called only after you thorougly chech your vars.
            IT HAS NO CHECKS AND WILL ONLY DO ITS THING.
            So beware and stuff. And have fun :>
        """

        def xgetter(theta): return self.x + (self.radius * np.cos(theta))
        def ygetter(theta): return self.y + (self.radius * np.sin(theta))
        # greater precision means more points. More points means greater processing time and greater circle resolution.
        thetas = np.linspace(0, 2*np.pi, self.precision)
        self.allx = []
        self.ally = []
        for theta in thetas:
            self.allx.append(xgetter(theta))
            self.ally.append(ygetter(theta))
