import numpy as np
import os
class random_nb:
    """Class to create random numbers"""

    def __init__(self, sw, n):
        """initialisation of parameters
        Args:
            sw = Sollwert
            n = Anzahl der Messungen
        Output:
            Random data: [a1,...,an]
            
        """
        self.sw = sw
        self.n = n

    def __repr__(self):
        return '%s("Sollwert = "%a,"Anzahl der Messungen" %a)' %(self.__class__.__name__, self.sw, self.n)
    
    def random_nb(self):
        cur_path = os.getcwd()
        path = os.getcwd()+"/data"
        s = 1
        x = np.random.normal(self.sw, s, size = self.n)
        a = np.around(x,decimals=1)
        print("cur_dir: ",os.getcwd())
        try:
            os.mkdir(path)
        except:
            os.chdir(path)
        np.savetxt("daten.txt", a, fmt='%2.1f')

        print("cur_dir: ",os.getcwd())
        b = np.loadtxt("daten.txt")
        print("Gespeicherte Messwerte ")
        print(a[:self.n//20])
        print("Messwerte auslesen")
        print(b[:self.n//20])
        os.chdir(cur_path)
        print("cur_dir: ",os.getcwd())

        
