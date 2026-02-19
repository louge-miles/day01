import unittest
import os
import importlib.util

# 动态导入 day01/01.py （文件名以数字开头，不能通过普通 import）
here = os.path.dirname(__file__)
module_path = os.path.join(here, "01.py")
spec = importlib.util.spec_from_file_location("module01", module_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sum_even = mod.sum_even

class TestSumEven(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 6]), 12)

    def test_empty(self):
        self.assertEqual(sum_even([]), 0)

    def test_nonints_ignored(self):
        self.assertEqual(sum_even([2, 3.0, 4, "6", None]), 6)

    def test_negatives(self):
        self.assertEqual(sum_even([-2, -3, 4]), 2)

if __name__ == "__main__":
    unittest.main()
