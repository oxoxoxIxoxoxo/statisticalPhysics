import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from library.random_nb import random_nb as rnb

a = rnb(50,1000)
print(a.random_nb())