import collections
from decimal import Decimal, ROUND_HALF_UP
class Vector:
    """

    """
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        products = tuple([coordinate*scalar for coordinate in self.coordinates ])
        return Vector(products)

    def magnitude(self):
        """Returns the magnitude of a Vector
            Using the pathagorean theorem
        """
        sum_squares = 0
        for coord in self.coordinates:
            sum_squares+= coord**2
        return sum_squares**0.5

    def direction(self):
        """Returns the direction of the function
            Unit vector in the direction of the vector
        """
        try:
            return self.scalar_multiply(self.magnitude()**-1)
        except ZeroDivisionError:
            raise ZeroDivisionError('zero vector has no direction')
    def round_coordinates(self, precision):
        """Round coordinates in a vector
           Uses decimal.ROUND_HALF_UP
        """
        if isinstance(precision, collections.Iterable):
            raise TypeError('value must not be iterable')
        def round_coordinate(coordinate):
            return float(Decimal(str(coordinate)).quantize(Decimal(precision_str), rounding=ROUND_HALF_UP))
        precision_str = '.{:0>{prec}d}'.format(1,prec=precision)
        self.coordinates = tuple([round_coordinate(coordinate) for coordinate in self.coordinates])

    def __str__(self):
        return str(self.coordinates)

    def __eq__(self, other):
        return self.coordinates==other.coordinates
