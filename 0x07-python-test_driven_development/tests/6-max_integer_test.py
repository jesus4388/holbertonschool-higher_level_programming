#!/usr/bin/python3
'# nteractive tests'

import unittest
max_integer = __import__('6-max_integer').max_integer
module = __import__('6-max_integer')

class TestMaxInt(unittest.TestCase):
    '# class TestMaxInt'

    def test_module(self):
        '# test doc modulo'
        self.assertTrue(len(module.__doc__), 1)

    def test_function(self):
        '# test doc function'
        self.assertTrue(len(max_integer.__doc__), 1)

    def test_maxinteger(self):
        '# test max integer'
        self.assertEqual(max_integer([1,2]), 2)

    def test_max(self):
        '# test max integer'
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)

    def test_float(self):
        '#test max float'
        self.assertEqual(max_integer([-3.5, -1.3, -2.2]), -1.3)



if __name__ == '__main__':
    unittest.main()
