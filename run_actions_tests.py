#! /usr/bin/env python

#
# The run_tests.py file aims at running all tests that are supposed to be executed within the application
#   at first we import the base library paths and then we run the tests
#

import unittest
import sys

sys.path.append("tests")

from test_navigation_actions import TabNavigationActionTest
from test_keyboard_actions import FillFocusedElementActionTest 
from test_js_code_loader import JsCodeLoaderTest

if __name__ == "__main__":
    unittest.main()
