import unittest
from decimal import Decimal, ROUND_HALF_UP
from linear_algebra.vector import Vector 

def round_float(coordinate, precision):
    """Simple helper function to round values just like
        the Vector method round_coordinate does
    """
    precision_str = '.{:0>{prec}d}'.format(1,prec=precision)
    return float(Decimal(str(coordinate)).quantize(Decimal(precision_str), rounding=ROUND_HALF_UP))
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
    
    def test_repr_single_dimension(self):
        self.assertEqual(repr(self.vector1d), "(Decimal('1'),)",'repr does not work')
    
    def test_repr_three_dimensions(self):
        self.assertEqual(repr(self.vector3d), "(Decimal('1'), Decimal('2'), Decimal('3'))",'repr does not work')
    
    def test_str_single_dimension(self):
        self.assertEqual(str(self.vector1d), "Vector: (1.0,)",'str does not work')
    
    def test_str_three_dimensions(self):
        self.assertEqual(str(self.vector3d), "Vector: (1.0, 2.0, 3.0)",'str does not work')

    def test_eq_three_dimensions(self):
        self.assertEqual(self.vector3d==Vector((1,2,3)), True,'eq does not work')
        self.assertEqual(Vector((-1,2,3))==self.vector3d, False,'eq does not work')
    
    def test_eq_float_3d(self):
        self.assertEqual(Vector((1.234, 4.543, 9.000)), Vector((1.234, 4.543, 9.000)), 'eq does not work')

    def test_eq_one_dimension(self):
        self.assertEqual(self.vector1d==Vector((1,)), True, 'eq does not work')
        self.assertEqual(self.vector1d==Vector((-1,)), False, 'eq does not work')
    
    def test_round_coordinates(self):
        vector = Vector((1.00001, 2.12348, -8274.125, 2))
        vector.round_coordinates(2)
        self.assertEqual(vector.coordinates, (Decimal('1.00'), Decimal('2.12'), Decimal('-8274.13'), Decimal('2.00')), 'round_coordinates does not work')
    
    def test_round_coordinates_assert(self):
        with self.assertRaises(TypeError, msg='round_coordinates does not throw TypeError if precision is iterable'):
                self.vector3d.round_coordinates((1,2,3))
    
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
    
    def test_magnitude_simple(self):
        result = Vector((2,2,2,2)).magnitude()
        self.assertEqual(result, 4, 'magnitude does not work')
    
    def test_magnitude_float_2d(self):
        result = Vector((-0.221, 7.437)).magnitude()
        self.assertEqual(round_float(result, 3), 7.440, 'magnitude does not work')
    
    def test_magnitude_float_3d(self):
        result = Vector((8.813, -1.331, -6.247)).magnitude()
        self.assertEqual(round_float(result, 3),10.884, 'magnitude does not work')
    
    def test_direction_simple(self):
        result = Vector((2,2,2,2)).direction()
        self.assertEqual(result, Vector((.5,.5,.5,.5)), 'direction does not work')
    
    def test_direction_assert(self):
        with self.assertRaises(ZeroDivisionError, msg='direction does not throw ZeroDivisionError if magnitude is 0'):
            Vector((0,0,0)).direction()
    
    def test_direction_float_2d(self):
        result = Vector((5.581, -2.136)).direction()
        result.round_coordinates(3)
        self.assertEqual(result, Vector((0.934, -0.357)), 'direction does not work')
    
    def test_direction_float_3d(self):
        result = Vector((1.996, 3.108, -4.554)).direction()
        result.round_coordinates(3)
        self.assertEqual(result, Vector((0.340,0.530,-0.777)), 'direction does not work')

    def test_dot_product_simple(self):
        v1 = Vector((1,2,-1))
        v2 = Vector((3,1,0))
        result = v1.dot_product(v2)
        self.assertEqual(result, 5, 'dot product does not work')

    def test_dot_product_float_2d(self):
        v1 = Vector((7.887,4.138))
        v2 = Vector((-8.802,6.776))
        result = v1.dot_product(v2)
        result = round_float(result, 3)
        self.assertEqual(result, -41.382, 'dot product does not work')

    def test_dot_product_float_3d(self):
        v1 = Vector((-5.955,-4.904,-1.874))
        v2 = Vector((-4.496, -8.755, 7.103))
        result = v1.dot_product(v2)
        result = round_float(result, 3)
        self.assertEqual(result, 56.397, 'dot product does not work')

    def test_angle_rad_simple(self):
        v1 = Vector((1,2,-1))
        v2 = Vector((3,1,0))
        result = v1.angle(v2)
        result = round_float(result, 2)
        self.assertEqual(result, 0.87, 'angle does not work')

    def test_angle_rad_float(self):
        v1 = Vector((3.183, -7.627))
        v2 = Vector((-2.668, 5.319))
        result = v1.angle(v2)
        result = round_float(result, 3)
        self.assertEqual(result, 3.072, 'angle does not work')

    def test_angle_degrees_simple(self):
        v1 = Vector((1,2,-1))
        v2 = Vector((3,1,0))
        result = v1.angle(v2, Vector.DEGREES)
        self.assertEqual(round(result), 50, 'angle does not work')
    def test_angle_same_vector(self):
        v1 = Vector((1,2,-1))
        result = v1.angle(v1)
        self.assertEqual(round(result), 0, 'angle does not work')
    
    def test_angle_degrees_float(self):
        v1 = Vector((7.35, 0.221, 5.188))
        v2 = Vector((2.751, 8.259, 3.985))
        result = v1.angle(v2, Vector.DEGREES)
        result = round_float(result, 3)
        self.assertEqual(result, 60.276, 'angle does not work')

    def test_angle_assert(self):
        with self.assertRaises(ZeroDivisionError, msg='angle does not throw ZeroDivisionError if magnitude of either vector is 0'):
            Vector((0,0,0)).angle(Vector((1,2,3)))
