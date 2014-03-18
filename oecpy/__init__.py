"""
Help?
"""
__version__ = '1.0b1.2'

import sys

# Import package modules
from . import assumptions, astroclasses, astroquantities, equations, example, flags
# import OEC database
from .database import OECDatabase


def test():
    if sys.hexversion < 0x02070000:
        import unittest2 as unittest
    else:
        import unittest

    from tests import testsuite as _testsuite
    unittest.TextTestRunner(verbosity=2).run(_testsuite)