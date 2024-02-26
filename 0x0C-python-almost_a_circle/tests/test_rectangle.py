#!/usr/bin/python3
"""
Unittest for the class Rectangle.
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Class for testing.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle()

    def test_more_args(self):
        """ Test for an instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle(1, 1, 1, 1, 1, 1)

    def test_less_args(self):
        """ Test for less arguments than required. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle(1)

    def test_correct_inst(self):
        """ Test for a correct instantiation. """
        rct1 = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(rct1.width, 3)
        self.assertEqual(rct1.height, 5)
        self.assertEqual(rct1.x, 1)
        self.assertEqual(rct1.y, 2)
        self.assertEqual(rct1.id, 45)
        rct1 = Rectangle(1, 2)
        self.assertEqual(rct1.width, 1)
        self.assertEqual(rct1.height, 2)
        self.assertEqual(rct1.x, 0)
        self.assertEqual(rct1.y, 0)

    def test_wrong_type_width(self):
        """ Test for a wrong type for width. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle("wrong", 5)

    def test_wrong_type_height(self):
        """ Test for a wrong type for height. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle(5, "wrong")

    def test_wrong_type_x(self):
        """ Test for a wrong type for x. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle(10, 5, "wrong")

    def test_wrong_type_y(self):
        """ Test for a wrong type for y. """
        with self.assertRaises(TypeError):
            rct1 = Rectangle(10, 5, 1, "wrong")

    def test_width_zero(self):
        """ Test for a width of 0. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(0, 5)

    def test_height_zero(self):
        """ Test for a height of 0. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(10, 0)

    def test_width_neg(self):
        """ Test for a negative width. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(-1, 5)

    def test_height_neg(self):
        """ Test for a negative height. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(5, -1)

    def test_x_neg(self):
        """ Test for a negative x. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(1, 5, -1)

    def test_y_neg(self):
        """ Test for a negative y. """
        with self.assertRaises(ValueError):
            rct1 = Rectangle(1, 5, 1, -1)

    def test_setters_ok(self):
        """ Test for setters with good values. """
        rct1 = Rectangle(1, 5)
        rct1.width = 2
        rct1.height = 6
        rct1.x = 3
        rct1.y = 4
        self.assertEqual(rct1.width, 2)
        self.assertEqual(rct1.height, 6)
        self.assertEqual(rct1.x, 3)
        self.assertEqual(rct1.y, 4)

    def test_width_setter_wrong(self):
        """ Test for wrong type for width setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            rct1.width = "wrong"

    def test_height_setter_wrong(self):
        """ Test for wrong type for height setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            rct1.height = "wrong"

    def test_x_setter_wrong(self):
        """ Test for wrong type for x setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            rct1.x = "wrong"

    def test_y_setter_wrong(self):
        """ Test for wrong type for y setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            rct1.y = "wrong"

    def test_width_setter_zero(self):
        """ Test with 0 for width setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.width = 0

    def test_height_setter_zero(self):
        """ Test with 0 for height setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.height = 0

    def test_width_setter_neg(self):
        """ Test with negative for width setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.width = -1

    def test_height_setter_neg(self):
        """ Test with negative for height setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.height = -1

    def test_x_setter_neg(self):
        """ Test with negative for x setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.x = -1

    def test_y_setter_neg(self):
        """ Test with negative for y setter. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(ValueError):
            rct1.y = -1

    def test_area_with_arg(self):
        """ Test calling area function with argument. """
        rct1 = Rectangle(1, 5)
        with self.assertRaises(TypeError):
            rct1.area(1)

    def test_area_ok(self):
        """ Test the area function. """
        rct1 = Rectangle(5, 7)
        r2 = Rectangle(1, 2)
        r3 = Rectangle(10, 5)
        self.assertEqual(rct1.area(), 35)
        self.assertEqual(r2.area(), 2)
        self.assertEqual(r3.area(), 50)

    def test_display_with_arg(self):
        """ Test calling display function with argument. """
        rct1 = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            rct1.display(1)

    def test_display_ok(self):
        """ Test the display function. """
        rct1 = Rectangle(2, 3, 1, 1)
        outrct1 = StringIO()
        with redirect_stdout(outrct1):
            rct1.display()
            self.assertEqual(outrct1.getvalue(), "\n ##\n ##\n ##\n")

    def test_str_rep(self):
        """ Test for string representation of a rectangle. """
        rct1 = Rectangle(3, 5, 1, 2, 45)
        self.assertEqual(rct1.__str__(), "[Rectangle] (45) 1/2 - 3/5")

    def test_update(self):
        """ Test for update method of rectangle. """
        rct1 = Rectangle(3, 5, 1, 2, 45)
        rct1.update(12, 9, 5, 5, 8)
        self.assertEqual(rct1.width, 9)
        self.assertEqual(rct1.height, 5)
        self.assertEqual(rct1.x, 5)
        self.assertEqual(rct1.y, 8)
        self.assertEqual(rct1.id, 12)
        rct1.update(23)
        self.assertEqual(rct1.id, 23)
        self.assertEqual(rct1.width, 9)
        self.assertEqual(rct1.height, 5)
        self.assertEqual(rct1.x, 5)
        self.assertEqual(rct1.y, 8)
        rct1.update(y=4, x=12, width=8, id=6, height=99)
        self.assertEqual(rct1.width, 8)
        self.assertEqual(rct1.height, 99)
        self.assertEqual(rct1.x, 12)
        self.assertEqual(rct1.y, 4)
        self.assertEqual(rct1.id, 6)
        rct1.update(x=1)
        self.assertEqual(rct1.x, 1)
        rct1.update(6, x=23)
        self.assertEqual(rct1.id, 6)
        self.assertEqual(rct1.x, 1)

    def test_to_dict(self):
        """ Test for to dictionary function. """
        rct1 = Rectangle(3, 5, 1, 2, 45)
        rct1_d = rct1.to_dictionary()
        dic = {'x': 1, 'width': 3, 'id': 45, 'y': 2, 'height': 5}
        self.assertDictEqual(rct1_d, dic)

    def test_to_dict_with_arg(self):
        """ Test calling to_dictonary function with argument. """
        rct1 = Rectangle(2, 1)
        with self.assertRaises(TypeError):
            rct1.to_dictionary(1)
