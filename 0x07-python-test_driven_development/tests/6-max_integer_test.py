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

    def test_string(self):
        '# test string'
        self.assertRaises(TypeError,lambda: max_integer([2, 5, "hello"]), 3)

    def test_float_positive(self):
        'test float'
        self.assertEqual(max_integer([3.5, 1.3, 2.2]), 3.5)

    def test_one_number_negative(self):
        '#test number negative'
        self.assertTrue(max_integer([1, 2, 3, -4]), 3)

    def test_none(self):
        '# test none'
        self.assertRaises(TypeError,lambda: max_integer([2, 5, None]), 3)

    def test_Bool(self):
        '# test none'
        self.assertRaises(TypeError,lambda: max_integer([2, 5, 4]), False)



if __name__ == '__main__':
    unittest.main()
