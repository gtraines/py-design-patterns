# Behavioral patterns - focus on the responsibility that an object has
#
# Observer pattern - an object (Subject) maintains a list of dependents
#                    (Observers) so that the Subject can notify all the Observers
#                    about changes that it undergoes using any of the methods
#                    defined by the Observer
#   Main intentions:
#   * Defines a 1:many dependency between objects so that any change in one
#       object will be notified to the other dependent objects automatically
#   * Encapsulates the core component of the Subject
#
#   
# Example use case:
#   E-mail service that observes the state of the user and sends e-mails to
#   the user.
#   Example events: User registration -> account verification email
#                   Verified account low on credits
#
# General applications: Broadcast, publish/subscribe system, Event service in
# distributed systems
#




