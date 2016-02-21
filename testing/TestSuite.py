__author__ = 'zhangb3'

import unittest
import os
import subprocess
import sys
from calculate import Calculate

Test_Script = os.getcwd() + os.sep + "calculate.py"
Config_Dir = "configurations" + os.sep

class FunctionTest(unittest.TestCase):
    def test_call_script(self):
        """Test basic function of this script"""
        cmd = Test_Script + " " + Config_Dir + "test.txt"
        out = os.system(cmd)
        self.assertEqual(out, 0)
        pass

    def test_function_print_result(self):
        myclass = Calculate()
        try:
            myclass.print_result(5, 10)
        except:
            self.fail("Can't call function print result successfully")
        pass

    def test_function_usage(self):
        myclass = Calculate
        try:
            myclass.usage()
        except:
            self.fail("fail to execute usage() function")

class NegativeTest(unittest.TestCase):
    def test_no_parameter(self):
        """ Script will fail if no parameter """
        cmd = Test_Script
        out = os.system(cmd)

if __name__ == '__main__':
    unittest.main()
