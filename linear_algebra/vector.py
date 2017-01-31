import collections
from decimal import Decimal, ROUND_HALF_UP
import math
class Vector:
    """

    """
    RADIANS = "radians"
    DEGREES = "degrees"
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(str(x)) for x in coordinates])
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be iterable')
    def plus(self, vector):
        sums = tuple([a+b for a, b in zip(self.coordinates, vector.coordinates) ])
        return Vector(sums)
        
    def minus(self, vector):
        differences = tuple([ a-b for a, b in zip(self.coordinates, vector.coordinates) ])
        return Vector(differences)

    def scalar_multiply(self, scalar):
        if isinstance(scalar, collections.Iterable):
            raise TypeError('value must not be iterable')
        products = tuple([coordinate*Decimal(str(scalar)) for coordinate in self.coordinates ])
        return Vector(products)

    def magnitude(self):
        """Returns the magnitude of a Vector
            Using the pathagorean theorem
        """
        sum_squares = Decimal('0')
        for coord in self.coordinates:
            sum_squares+= coord**Decimal('2')
        return sum_squares**Decimal('0.5')

    def direction(self):
        """Returns the direction of the function
            Unit vector in the direction of the vector
        """
        try:
            return self.scalar_multiply(self.magnitude()**Decimal(str('-1')))
        except:
            raise ZeroDivisionError('zero vector has no direction')
    def dot_product(self, vector):
        return sum( a*b for a,b in zip(self.coordinates, vector.coordinates))

    def angle(self, vector, unit=None):
        try:
            theta = math.acos(self.dot_product(vector)/(self.magnitude()*vector.magnitude()))
        except:
            raise ZeroDivisionError("Angle cannot take a vector with magnitude zero")
        if unit==Vector.RADIANS or unit==None:
            return theta
        else:
            return math.degrees(theta)
    def round_coordinates(self, precision):
        """Round coordinates in a vector
           Uses decimal.ROUND_HALF_UP
        """
        if isinstance(precision, collections.Iterable):
            raise TypeError('value must not be iterable')
        def round_coordinate(coordinate):
            return Decimal(str(coordinate)).quantize(Decimal(precision_str), rounding=ROUND_HALF_UP)
        precision_str = '.{:0>{prec}d}'.format(1,prec=precision)
        self.coordinates = tuple([round_coordinate(coordinate) for coordinate in self.coordinates])

    def __str__(self):
        return "Vector: {}".format(self._to_floats())

    def __repr__(self):
        return repr(self.coordinates)

    def _to_floats(self):
        return tuple([float(x) for x in self.coordinates])

    def __eq__(self, other):
        return self.coordinates==other.coordinates
