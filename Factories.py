from abc import ABCMeta, abstractmethod # ABC is the Py metaklass to make a class Abstract

class Animal(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print "Woof woof"

class Cat(Animal):
    def speak(self):
        print "Meow, meow"

## forest factory defined
class ForestFactory(object):
    def make_sound(self, type_name):
        return eval(type_name)().speak()

## client code

if __name__ == '__main__':
    forest_factory = ForestFactory()
    animal_concrete = raw_input("Object type: ")
    forest_factory.make_sound(animal_concrete)


class Section(object):
    __metaclass__ = ABCMeta # makes class abstract
    _description = ""

    def __init__(self, section_name = ""):
        self._description = section_name
        return

    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def __init__(self):
        Section.__init__(self, "Personal")
        return

    def describe(self):
        return self._description

class PublicationSection(Section):
    def __init__(self):
        Section.__init__(self, "Publications")
        return

    def describe(self):
        return self._description


pers = PersonalSection()
print pers.describe()

pubs = PublicationSection()
print pubs.describe()


class Profile(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

class LinkedIn(Profile):
    # This is the concrete factory method
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PublicationSection())

if __name__ == '__main__':
    profile = eval("LinkedIn")()
    print type(profile).__name__
    print profile.getSections()


# Abstract Factory
# Makes sure the client is isolated from the creation of objects
# but allowed to use the objects created
# Client has the ability to access objects only through
# an interface


class AbstractProduct(object):
    __metaclass__ = ABCMeta
    _property_name = []

    @abstractmethod
    def getProperty(self):
        pass

class AnotherAbstractProduct(object):
    __metaclass__ = ABCMeta
    _another_property_name = []

    @abstractmethod
    def getAnotherProperty(self):
        pass

class ConcreteProduct(AbstractProduct):

    def __init__(self):
        AbstractProduct._property_name.append("PropertyItem")

    def getProperty(self):
        return AbstractProduct._property_name

class AnotherConcreteProduct(AnotherAbstractProduct):

    def __init__(self):
        AnotherAbstractProduct._another_property_name.append("AnotherPropertyItem")

    def getAnotherProperty(self):
        return AnotherAbstractProduct._another_property_name

# this abstract factory has no implementation details --
# it is the equivalent of an interface
class AbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def createProduct(self):
        pass

    @abstractmethod
    def createAnotherProduct(self):
        pass

class ConcreteFactoryOne(AbstractFactory):

    def createProduct(self):
        return # new concrete product of a type implementing abstract product

    def createAnotherProduct(self):
        return # new concrete "another" product of a type implementing abstract "another" product

class ConcreteFactoryTwo(AbstractFactory):

    def createProduct(self):
        return # concretion of the abstract product that this factory creates

    def createAnotherProduct(self):
        return # the concretion of another abstract product as provided by this factory

