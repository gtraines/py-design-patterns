"""
From Mark Lutz's _Programming Python_
"""

class Stack(list):
    "a list with extra methods"
    def top(self):
        return self[-1]

    def push(self, item):
        list.append(self, item)

    def pop(self):
        if not self:
            return None # avoid exception
        else:
            return list.pop(self)

class Set(list):
    "list with Set constraints and operations"
    def __init__(self, value=[]):
        list.__init__(self) # base class constructor
        self.concat(value)

    def intersect(self, other): # takes any sequence type as an arg
        result = []
        for x in self:
            if x in other:
                result.append(x)
        return Set(result) # returns a new Set instance with the matching elements

    def union(self, other):
        result = Set(self) # copy of existing set
        result.concat(other)

    def concat(self, value):
        "filter non-unique elements"
        for x in value:
            if not x in self:
                self.append(x)

    """
    override methods
    """
    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __str__(self):
        return '<Set:' + repr(self) + '>'




