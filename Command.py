from abc import ABCMeta, abstractmethod
# -*- coding: utf-8 -*-

# Command object -- knows about the Receiver objects and invokes a method of the Receiver object
# Values for parameters of the receiver method are stored in the Command object
# Invoker knows how to execute a command
# The client creates a Command object and sets its receiver

class Wizard(object):
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
        
    def preferences(self, command):
        self.choices.append(command)
        
    def execute(self):
        for choice in self.choices:
            if list(choice.values()[0]):
                print "Copying binaries ", self.src, " to ", self.rootdir
            else:
                print "No operation"
                
# Command: declares an interface to execute an operation
# ConcreteCommand: defines a binding between the Receiver object and an action
# Client: creates a ConcreteCommand object and sets it Receiver
# Invoker: asks ConcreteCommand to carry out the request
# Receiver: knows how to perform the operations associated with carrying out the request

class AbstractCommand(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, recv):
        self.recv = recv
        
    @abstractmethod
    def execute(self):
        pass
        

class Command(AbstractCommand):
    def execute(self):
        self.recv.action()


class Receiver(object):
    def action(self):
        print "Receiver action"
        

class Invoker(object):
    def command(self, cmd):
        self.cmd = cmd
        
    def execute(self):
        self.cmd.execute()
        
        