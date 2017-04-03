# -*- coding: utf-8 -*-

# Adapted from Nystrom's _Game Programming Patterns_

# * Fixed set of states that the machine can be in
# * Machine can only be in one state at a time
# * Sequence of inputs is sent to the machine
# * Each state has a set of "Transitions," each associated with an input
#   and pointing to a State

# States - Inputs - Transitions
from abc import ABCMeta, abstractmethod

class ItemState(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def handleInput(self, item, input_signal):
        # if using the update method, return the new state if applicable
        pass
    
    @abstractmethod
    def update(self, item):
        pass
    
    @abstractmethod
    def enter(self, item):
        # a single State may have multiple points of entry
        # from other states; following generation from the state graph
        # the other states can call this method
        pass
    
# For each state, we define a class that implements the interface

class ConcreteStateOne(ItemState):
    
    def __init__(self, state_specific_var):
        self._state_specific_var = state_specific_var
        
    def handleInput(self, item, input_signal):
        # implementation
        # determines how/whether this state handles the input signal
        pass
    
    def update(self, item):
        # implementation
        # set next state (if applicable) onto the item
        pass
    
    def enter(self, item):
        # implementation
        # perform whatever state-specific logic sets the item to
        # this state
        pass

class Item(object):
    __state = None # Probably should init with some dynamically
                    # determined state

    def __init__(self):
        self.__state = ConcreteStateOne("something about this")
    
    def handleInput(self, input_signal):
        self.__state.handleInput(self, input_signal)
        # maybe replace the state with the new state
        self.__state = self.__state.handleInput(self, input_signal)
    
    def update(self):
        self.__state.update(self)
        

# Nystrom: "If your state has no fields and only ONE virtual method in it,
#           you can simplify this pattern even more. Replace each state
#           *class* with a state *function* -- just a top-level function
#           Then, the __state field in your main class becomes a 
#           function pointer"

# "When you dynamically allocate states, you may have to worry about
#  fragmentation. The *Object pool* pattern can help"
        
    
    
    