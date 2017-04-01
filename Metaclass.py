# Metaclass = class of a class; a class is an instance of its metaclass
# Allows creation of user-defined classes from predefined Python classes

""" Python's __call__ method gets called when
an object needs to be created for an already existing class"""

class IntKlass(type):
    def __call__(cls, *args, **kwargs):
        print("Here's my int: ", args)
        return type.__call__(cls, *args, **kwargs)


class int(object):
    __metaclass__ = IntKlass
    __private_var = "Value"
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)

print(type(i))
print "x: ", i.x
print "y: ", i.y
