import io
from itertools import product
import math
import sys
from typing import Any, Callable, Tuple
import unittest

from main import *

class TestRun:
    def __init__(self,
                 testcase: unittest.TestCase,
                 ans: Any,
                 func: Callable,
                 call_args: Tuple[Any] = tuple()) -> None:
        self.testcase = testcase
        self.func = func
        self.call_args = call_args
        self.ans = ans
        self.result = func(*call_args)
    
    def callstr(self) -> str:
        return (
            f"{self.func.__name__}"
            f"({', '.join(repr(self.call_args) for arg in self.call_args)})"
        )
    
    def test(self) -> None:
        callstr = self.callstr()
        if self.ans is not None:
            self.testcase.assertIsNotNone(
                self.result,
                msg=f"{callstr} returned None"
            )
        self.testcase.assertIsInstance(
            self.result, type(self.ans),
            msg=f"{callstr} returned {type(self.result)}, expected {type(self.ans)}"
        )
        self.testcase.assertEqual(
            self.result, self.ans,
            msg=f"{callstr}: Got {self.result!r}, expected {self.ans!r}"
        )
        # Check docstring
        self.testcase.assertTrue(hasattr(self.func, "__doc__"), msg=f"{callstr} has no docstring")
        self.testcase.assertTrue(self.func.__doc__, msg=f"{callstr} has no docstring")


class TestAssignment(unittest.TestCase):

    def test_gcf(self):
        for a, b in product(range(1, 100), range(1, 100)):
            TestRun(self, ans=math.gcd(a, b), func=gcf, call_args=(a, b)).test()

    def test_lcm(self):
          for a, b in product(range(1, 100), range(1, 100)):
              TestRun(self, ans=(a * b // math.gcd(a, b)), func=lcm, call_args=(a, b)).test()

    def test_clock(self):
        stdout = io.StringIO()
        sys.stdout = stdout
        clock(3)
        sys.stdout = sys.__stdout__
        output = stdout.getvalue()
        
        self.assertFalse('\n' in output,
                         msg="The time should be printed on a single line only. Each new timing should overwrite the previous line. (Hint: Use the \\r carriage return special character)")
        self.assertTrue('\r' in output,
                        msg="The time should be printed on a single line only. Each new timing should overwrite the previous line. (Hint: Use the \\r carriage return special character)")
        
        for time in output.split('\r'):
            if not time:
                continue
            self.assertTrue(':' in time,
                            msg="Incorrect time format")
            time_components = time.split(':')
            self.assertEqual(len(time_components), 3)
            
            h, m, s = time_components
            self.assertTrue(h.isdecimal(),
                            msg="Incorrect time format")
            self.assertTrue(0 <= int(h) < 24,
                            msg="Invalid hour value")
            self.assertTrue(m.isdecimal(),
                            msg="Incorrect time format")
            self.assertTrue(0 <= int(m) < 60,
                            msg="Invalid minute value")
            self.assertTrue(s.isdecimal(),
                            msg="Incorrect time format")
            self.assertTrue(0 <= int(s) < 60,
                            msg="Invalid second value")

    def test_docstrings(self):
        for func in [gcf, lcm, clock]:
            self.assertIs(hasattr(func, "__doc__"), True)
            self.assertTrue(func.__doc__, f"{func.__name__}() does not have a docstring")


if __name__ == '__main__':
    unittest.main()
