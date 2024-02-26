#!/usr/bin/python3
"""
Unittest for class square.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for tests.
    """

    def test_empty(self):
        """ Test for an empty instantiation. """
        with self.assertRaises(TypeError):
            sq1 = Square()

    def test_more_args(self):
        """ Test for an instantiation with 1 more argument. """
        with self.assertRaises(TypeError):
            sq1 = Square(1, 1, 1, 1, 1)

    def test_correct_insta(self):
        """ Test for a correct instantiation. """
        sq1 = Square(3, 1, 2, 45)
        self.assertEqual(sq1.size, 3)
        self.assertEqual(sq1.x, 1)
        self.assertEqual(sq1.y, 2)
        self.assertEqual(sq1.id, 45)

    def test_str_rep(self):
        """ Test for string representation of a square. """
        sq1 = Square(3, 1, 2, 45)
        self.assertEqual(sq1.__str__(), "[Square] (45) 1/2 - 3")

    def test_size_setter(self):
        """ Test for size setter of square class. """
        sq1 = Square(3, 1, 2, 45)
        sq1.size = 27
        self.assertEqual(sq1.size, 27)

    def test_update(self):
        """ Test for update method. """
        sq1 = Square(3, 1, 2, 45)
        sq1.update(12, 5, 5, 8)
        self.assertEqual(sq1.size, 5)
        self.assertEqual(sq1.x, 5)
        self.assertEqual(sq1.y, 8)
        self.assertEqual(sq1.id, 12)
        sq1.update(23)
        self.assertEqual(sq1.id, 23)
        self.assertEqual(sq1.size, 5)
        self.assertEqual(sq1.x, 5)
        self.assertEqual(sq1.y, 8)
        sq1.update(y=4, x=12, size=8, id=6)
        self.assertEqual(sq1.size, 8)
        self.assertEqual(sq1.x, 12)
        self.assertEqual(sq1.y, 4)
        self.assertEqual(sq1.id, 6)
        sq1.update(x=1)
        self.assertEqual(sq1.x, 1)
        sq1.update(6, x=23)
        self.assertEqual(sq1.id, 6)
        self.assertEqual(sq1.x, 1)

    def test_to_dict(self):
        """ Test for to_dictionary function. """
        sq1 = Square(3, 1, 2, 45)
        sq1_d = sq1.to_dictionary()
        self.assertDictEqual(sq1_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})

    def test_wrong_size(self):
        """ Test for wrong type for size. """
        with self.assertRaises(TypeError):
            sq1 = Square("Wrong type")

    def test_size_zero(self):
        """ Test for a size of zero. """
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_wrong_type_x(self):
        """ Test for a wrong type for x. """
        with self.assertRaises(TypeError):
            sq1 = Square(10, "Wrong type")

    def test_wrong_type_y(self):
        """ Test for a wrong type for y. """
        with self.assertRaises(TypeError):
            sq1 = Square(10, "Wrong type")

    def test_size_neg(self):
        """ Test for a negative size. """
        with self.assertRaises(ValueError):
            sq1 = Square(-1)

    def test_x_neg(self):
        """ Test for a negative x. """
        with self.assertRaises(ValueError):
            sq1 = Square(1, -1)

    def test_y_neg(self):
        """ Test for a negative y. """
        with self.assertRaises(ValueError):
            sq1 = Square(1, 1, -1)

    def test_to_dict_with_arg(self):
        """ Test calling to_dictionary function with argument. """
        sq1 = Square(2)
        with self.assertRaises(TypeError):
            sq1.to_dictionary(1)
