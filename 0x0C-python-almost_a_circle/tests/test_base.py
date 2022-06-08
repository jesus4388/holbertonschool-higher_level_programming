#!/usr/bin/python3
'# interactive test'

import unittest
from models.base import Base
from contextlib import redirect_stdout
from models.rectangle import Rectangle
import io
import json


class test_base(unittest.TestCase):
    '# clss test base'

    def test_function(self):
        '# test doc function'
        self.assertTrue(len(Base.__doc__), 1)

    def test_id_empty(self):
        '# test id empty'
        self.assertEqual(Base(1).id, 1)

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
        self.assertEqual(Base(True).id, 1)

    def test_Bool_false(self):
        '# test id False'
        self.assertFalse(Base(False).id, 1)

    def test_json(self):
        '# test return string representation of json'
        self.r1 = Rectangle(10, 7, 2, 8)
        self.dictionary = self.r1.to_dictionary()
        self.json_dictionary = Base.to_json_string([self.dictionary])
        
        with redirect_stdout(io.StringIO()) as f:
            print(self.json_dictionary)
        self.assertEqual(f.getvalue(), '[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10}]\n')
        '# test type'
        self.assertEqual(type(f.getvalue()), str)

        '# test None'
        self.assertEqual(Base.to_json_string([None]), '[null]')

        '# test Empty'
        self.assertEqual(Base.to_json_string(['']),'[""]')

        '# save an empty list'
        self.assertFalse(Rectangle.save_to_file([]), [])

    def test_save_to_file(self):
        '# writes the JSON string representation of list_objs to a file:'
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        Rectangle.save_to_file([self.r1, self.r2])

        with open("Rectangle.json") as f:
            self.read = f.read()
        self.assertEqual(self.read, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')

        '# test type'
        self.assertEqual(type(self.read), str)


    def from_json_string(self):
        '# returns the list of the JSON string representation json_string'
        Base._Base__nb_objects = 0
        self.list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        self.json_list_input = Rectangle.to_json_string(self.list_input)
        self.list_output = Rectangle.from_json_string(self.json_list_input)

        with redirect_stdout(io.StringIO()) as f:
            print(self.list_output)
        self.assertEqual(f.getvalue(), "[{'height': 35, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]\n")

    if __name__ == "__main__":
        unittest.main()
