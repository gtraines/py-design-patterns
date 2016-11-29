""" Ch. 2: Singleton Pattern
"""

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

# Lazy Instantiation Singleton

class LazySingleton(object):
    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

ls = LazySingleton() ## class initialized but object not created
print("Object created", LazySingleton.getInstance())

ls1 = LazySingleton() # Instance already created
