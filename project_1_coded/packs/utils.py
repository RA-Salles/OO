"""
this little guy gives the program some incapsulated funcs for some utilities very very basic
"""


def numberparse(somestring: str, **kwargs):
    error = 0
    x = 0
    y = 0
    somestring.strip()
    if 'separator' in kwargs:
        try:
            zetta = somestring.split(str(kwargs['separator']))
        except:
            error = 1
    else:
        try:
            zetta = somestring.split(',')
        except:
            error = 1
    if error == 0:
        return zetta
    else:
        return "error"
