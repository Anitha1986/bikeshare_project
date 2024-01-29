""" file docstring - addition of two numbers """

import os
import sys

from script import addition

sys.path.insert(0, os.getcwd())


def add_test():
    """to test pytest"""
    subj = addition(7, 9)
    assert subj == 16
    print(subj)


add_test()
