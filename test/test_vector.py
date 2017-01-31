import unittest
from linear_algebra.vector import Vector 

class VectorTestCase(unittest.TestCase):
    def setUp(self):
        self.vector1d = Vector((1,))
        self.vector3d = Vector((1,2,3))

    def test_init_simple_case(self):
        self.assertEqual(self.vector3d.coordinates, (1,2,3), 'init does not work-coordinates incorrect')
        self.assertEqual(self.vector3d.dimension, 3, 'init does not work-dimension incorrect')
    def test_init_one_dimension(self):
        self.assertEqual(self.vector1d.coordinates, (1,),'init does not work-coordinates incorrect')
        self.assertEqual(self.vector1d.dimension, 1, 'init does not work-dimension incorrect')
    def test_init_empty_tuple(self):
        with self.assertRaises(ValueError, msg='init does not throw ValueError if coordinates are empty'):
                Vector( () )
    def test_init_not_iterable(self):
        with self.assertRaises(TypeError, msg='init does not throw TypeError if coordinates are not iterable'):
                Vector( 1 )
    def test_str_single_dimension(self):
        self.assertEqual(str(self.vector1d), "(1,)",'str does not work')
    def test_str_three_dimensions(self):
        self.assertEqual(str(self.vector3d), "(1, 2, 3)",'str does not work')
    def test_eq_three_dimensions(self):
        self.assertEqual(self.vector3d==Vector((1,2,3)), True,'eq does not work')
        self.assertEqual(Vector((-1,2,3))==self.vector3d, False,'eq does not work')
    def test_eq_one_dimension(self):
        self.assertEqual(self.vector1d==Vector((1,)), True, 'eq does not work')
        self.assertEqual(self.vector1d==Vector((-1,)), False, 'eq does not work')
    def test_plus_1d(self):
        self.assertEqual(self.vector1d.plus(Vector((-1,))), Vector((0,)), 'plus does not work')
        self.assertEqual(self.vector1d, Vector((1,)), 'plus does not work - changes vector')
    def test_plus_3d(self):
        self.assertEqual(self.vector3d.plus(Vector((-1,2,3))), Vector((0,4,6)), 'plus does not work')
        self.assertEqual(self.vector3d, Vector((1,2,3)), 'plus does not work - changes vector')
    def test_minus_1d(self):
        self.assertEqual(self.vector1d.minus(Vector((-1,))), Vector((2,)), 'minus does not work')
        self.assertEqual(self.vector1d, Vector((1,)), 'plus does not work - changes vector')
    def test_minus_1d(self):
        self.assertEqual(self.vector3d.minus(Vector((-1,2,3))), Vector((2,0,0)), 'minus does not work')
        self.assertEqual(self.vector3d, Vector((1,2,3)), 'plus does not work - changes vector')
    def test_scalar_multiplication_1d(self):
        self.assertEqual(self.vector1d.scalar_multiply(-1), Vector((-1,)), 'scalar multiply does not work')
        self.assertEqual(self.vector1d, Vector((1,)), 'scalar multiply does not work - changes vector')
    def test_scalar_multiplication_3d(self):
        self.assertEqual(self.vector3d.scalar_multiply(-1), Vector((-1,-2,-3)), 'scalar multiply does not work')
        self.assertEqual(self.vector3d, Vector((1,2,3)), 'scalar multiply does not work - changes vector')
    def test_scalar_multiply_assert(self):
        with self.assertRaises(TypeError, msg='scalar_multiply does not throw TypeError if scalar is iterable'):
                self.vector3d.scalar_multiply((1,2,3))
    def test_plus_float(self):
        v1 = Vector((8.218, -9.341))
        v2 = Vector((-1.129, 2.111))
        resultV = v1.plus(v2)
        resultV.round_coordinates(3)
        self.assertEqual(resultV, Vector((7.089,-7.230)), 'plus does not work')
    def test_minus_float(self):
        v1 = Vector((7.119, 8.215))
        v2 = Vector((-8.223, 0.878))
        resultV = v1.minus(v2)
        resultV.round_coordinates(3)
        self.assertEqual(resultV, Vector((15.342,7.337)), 'minus does not work')
    def test_scalar_multiply_float(self):
        v1 = Vector((1.671, -1.012, -0.318))
        scalar = 7.41
        resultV = v1.scalar_multiply(scalar)
        resultV.round_coordinates(3)
        self.assertEqual(resultV, Vector((12.382,-7.499,-2.356)), 'scalar multiply does not work')
