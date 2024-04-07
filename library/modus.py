import numpy as np
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from scipy.stats import mode
os.chdir('../Test/data')

class modus:
    def __init__(self, path):
        self.path = path

    def modus(self):

        a = np.loadtxt(self.path)
        m = mode(a)
        print("Die Masse %sg kommt %s mal vor" %(m[0][0], m[1][0]))