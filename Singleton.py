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

# Monostate Pattern

class Monostate(object):
    __shared_state = { "1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

# Borg Pattern
class Borg(object):
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

class HealthCheck(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck.__instance:
            HealthCheck.__instance \
                = super(HealthCheck, cls)\
                    .__new__(cls, *args, **kwargs)
        return HealthCheck.__instance

    def __init__(self):
        self.__servers = []

    def addServer(self):
        if len(self.__servers) == 0:
            self.__servers.append("Server Instance 1")
            self.__servers.append("Server Instance 3")
            self.__servers.append("Server Instance 4")
            self.__servers.append("Server Instance 2")

    def changeServer(self, server_name):
        self.__servers.pop()
        self.__servers.append(server_name)

    def getServers(self):
        return self.__servers


health_check_1 = HealthCheck()
health_check_2 = HealthCheck()

health_check_1.addServer()
for i in range(len(health_check_2.getServers())):
    print "Checking ", health_check_1.getServers()[i]

health_check_2.addServer()
health_check_2.changeServer("Server Instance 5")
for i in range(len(health_check_1.getServers())):
    print "Checking ", health_check_2.getServers()[i]