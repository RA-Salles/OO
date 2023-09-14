

class point():
    # this little guy will store like... everything for everyone.
    major_vector = []

    def __init__(self, x, y):
        self.makemajorvector(zetta=[x, y])

    def makemajorvector(self, **kwargs):
        for arg in kwargs:  # i expect this dude to gather everything passed and that's that
            # but i'm almost sure this here won't work
            self.major_vector.append(kwargs[arg])


class line(point):  # i actually shouldn't make this guy get any inheritance :> BECAUSE LINE CONTAINS MANY POINTS BUT ARE INHERENTLY DIFFERENT!!!!!!
    def __init__():
        pass

    def precisiongetter():
        pass

    def die():
        pass
    pass


class figure(line):
    def __init__():
        self.major_vector = []

    pass
