import numpy as np

class random_nb:
    """Class to create random numbers"""

    def __init__(self, sw, n):
        """initialisation of parameters
        Args:
            sw = Sollwert
            n = Anzahl der Messungen
        Output:
            
        """
        self.sw = sw
        self.n = n

    def __repr__(self):
        return '%s("Sollwert = "%a,"Anzahl der Messungen" %a)' %(self.__class__.__name__, self.sw, self.n)
    
    #def random_nb():
        
