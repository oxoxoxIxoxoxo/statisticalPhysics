import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from library.sortieren import sortieren as sort
from library.random_nb import random_nb
random = random_nb(50,1000)
rand_nb = random.random_nb()
sortiere = sort(rand_nb)
sorted_bubble = sortiere.bubble_sort()
sorted_selection = sortiere.selectionSort()
print(sorted_bubble)
#print(sorted_selection)