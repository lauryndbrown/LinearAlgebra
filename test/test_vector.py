import unittest
from linear_algebra.vector import Vector 

class VectorTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_init_simple_case(self):
        vector = Vector((1,2,3))
        self.assertEqual(vector.coordinates, (1,2,3), 'init does not work-coordinates incorrect')
        self.assertEqual(vector.dimension, 3, 'init does not work-dimension incorrect')
    def test_init_one_dimension(self):
        vector = Vector((1, ))
        self.assertEqual(vector.coordinates, (1,),'init does not work-coordinates incorrect')
        self.assertEqual(vector.dimension, 1, 'init does not work-dimension incorrect')
    def test_init_empty_tuple(self):
        with self.assertRaises(ValueError, msg='init does not throw ValueError if coordinates are empty'):
                Vector( () )
    def test_init_not_iterable(self):
        with self.assertRaises(TypeError, msg='init does not throw TypeError if coordinates are not iterable'):
                Vector( 1 )
    def test_str_single_dimension(self):
        vector = Vector((1, ))
        self.assertEqual(str(vector), "(1,)",'str does not work')
    def test_str_three_dimensions(self):
        vector = Vector((1,2,3 ))
        self.assertEqual(str(vector), "(1, 2, 3)",'str does not work')
    def test_eq_three_dimensions(self):
        self.assertEqual(Vector((1,2,3))==Vector((1,2,3)), True,'eq does not work')
        self.assertEqual(Vector((-1,2,3))==Vector((1,2,3)), False,'eq does not work')
    def test_eq_one_dimension(self):
        self.assertEqual(Vector((1,))==Vector((1,)), True, 'eq does not work')
        self.assertEqual(Vector((1,))==Vector((-1,)), False, 'eq does not work')
