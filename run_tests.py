#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Run all tests"

import sys, os, re
import unittest

TESTED_CODE = "src/"  # Path to tested code.
TESTS   = "test/" # Path to test code.

sys.path.append(TESTED_CODE)
sys.path.append(TESTS)

# Import all the tests from 'test/'.
for testFile in os.listdir(TESTS):
    if re.match("^test_.+\.py$", testFile):
        exec "from %s import *" % testFile[0:-3]

# Run the tests.
if __name__ == "__main__":
    unittest.main()
