# Defining a new class with 2 'special' double 
# underscore methods and one normal method.
# This class will have an attribute "x" that is 
# specified at the time of creating new instances 
# of the class

class A:
    """Base class."""

    def __init__(self, x):
        self.x = x
    
    def __repr__(self):
        return '%s(%a)' %(self.__class__.__name__, self.x)
    
    def report(self):
        """Report type of contained value."""

        return 'My value is of type %s' % type(self.x)