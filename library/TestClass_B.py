import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from library.TestClass_A import A

class B(A):
    """Derived class inherits from A."""

    def report(self):
        """Overwrite report() method of A"""
        return self.x