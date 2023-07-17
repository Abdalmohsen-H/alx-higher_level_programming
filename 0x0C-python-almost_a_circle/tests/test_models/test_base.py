#!/usr/bin/python3
'''
a py file for testing base.py in models module
using unittest
'''


from model.base import Base
import unittest



class test_base(unittest.TestCase):
    ''' test case using unittesting '''
    def test_sfsg(self):
        self.assertEqual(Base(12), 12, "should be 12")

if "__main__" == __name__:
    unittest.main()
