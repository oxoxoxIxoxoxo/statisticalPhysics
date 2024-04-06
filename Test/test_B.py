import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from library.TestClass_B import *
from library.TestClass_A import *

a0 = A(x = 3.14)

print(B.__doc__)
b0 = B(3+4j)
b1 = B(x = a0)

print(b0.x, b1.x)
print(b1.x.report())
