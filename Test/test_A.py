import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from library.TestClass_A import A

a0 = A(x = 3.14)
print("value: ", a0.x, "report-Method: ", a0.report())
