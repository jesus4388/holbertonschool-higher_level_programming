#%/usr/bin/python3
'# interactive test'

import unittest
from models.base import Base
from contextlib import redirect_stdout
from models.rectangle import Rectangle
import io


class test_base(unittest.TestCase):
    '# clss test base'

    def test_function(self):
        '# test doc function'
        self.assertTrue(len(Base.__doc__), 1)

    def test_id_empty(self):
        '# test id empty'
        self.assertTrue(Base(1).id, 1)

    def test_id_integer(self):
        '# test id integer'
        self.assertEqual(Base(12).id, 12)

    def test_id_str(self):
        '# test id str'
        self.assertRaises(TypeError,lambda: Base("hello").id, 2)

    def test_id(self):
        '# test id'
        self.assertRaises(TypeError,lambda: Base(12), 12)

    def test_id_negative(self):
        '# test negative'
        self.assertEqual(Base(-12).id, -12)

    def test_id_none(self):
        '# test id none'
        self.assertEqual(Base(None).id, 1)

    def test_Bool(self):
        '# test id booleano'
        self.assertTrue(Base(True).id, 1)

    def test_Bool_false(self):
        '# test id False'
        self.assertFalse(Base(False).id, 1)

    def test_json(self):
        '# test return string representation of json'
            r1 = Rectangle(10, 7, 2, 8)
            dictionary = r1.to_dictionary()
            self.assertEqual(Base.to_json_string([dictionary]), [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])

    def test_json1(self):
        '#  test return string representation of json'
            r1 = Rectangle(10, 7, 2, 15)
            dictionary = r1.to_dictionary()
            r2 = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 15}]
            self.assertEqual(Base.to_json_string([dictionary]), r2)

    def test_dict_None(self):
        '# test None'
        self.assertTrue(Base.to_json_string([None]),[])

    def test_dict_Empty(self):
        '# test Empty'
        self.assertTrue(Base.to_json_string(['']),[])

    def test_integer_negative(self):
        '# test negative'
        r1 = {'x': -2, 'width': -10, 'id': -1, 'height': -7, 'y': 8}
        r2 = Base.to_json_string
        r3 = [{"x": -2, "width": -10, "id": -1, "height": -7, "y": 8}]

        self.assertTrue(Base.to_json_string([r1]), r1)

    def test_list_empty(self):
        '# save an empty list'
        from models.rectangle import Rectangle
            r1 = Rectangle()
            r2 = Rectangle()
            self.assertTrue(Rectangle.save_to_file([r1], [r2]), [])

    def test_list_none(self):
        '# save an empty list'
        from models.rectangle import Rectangle
            r1 = Rectangle(None)
            r2 = Rectangle(None)
            self.assertTrue(Rectangle.save_to_file([r1], [r2]), 22)

    def test_list_integer(self):
        '# save an list'
        from models.rectangle import Rectangle
            r1 = Rectangle(10, 7, 2, 8)
            r2 = Rectangle(2, 4)
            self.assertTrue(Rectangle.save_to(r1, r2), 23)
