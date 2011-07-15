#! /usr/bin/env python

#
# The run_tests.py file aims at running all tests that are supposed to be executed within the application
#   at first we import the base library paths and then we run the tests
#

import unittest
import sys

sys.path.append("libs")
sys.path.append("tests")

if __name__ == "__main__":
    unittest.main()
