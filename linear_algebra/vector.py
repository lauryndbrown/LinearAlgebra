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
        sums = tuple([ float(Decimal(str(a))+Decimal(str(b))) for a, b in zip(self.coordinates, vector.coordinates) ])
        return Vector(sums)
        
    def minus(self, vector):
        differences = tuple([float(Decimal(str(a))-Decimal(str(b))) for a, b in zip(self.coordinates, vector.coordinates) ])
        return Vector(differences)

    def scalar_multiply(self, scalar):
        if isinstance(scalar, collections.Iterable):
            raise TypeError('value must not be iterable')
        products = tuple([float(Decimal(coordinate)*Decimal(scalar)) for coordinate in self.coordinates ])
        return Vector(products)

    def round_coordinates(self, precision):
        def round_coordinate(coordinate, precision):
            return float(Decimal(str(coordinate)).quantize(Decimal(precision_str), rounding=ROUND_HALF_UP))
        if isinstance(precision, collections.Iterable):
            raise TypeError('value must not be iterable')
        precision_str = '.{:0>{prec}d}'.format(1,prec=precision)
        self.coordinates = tuple([round_coordinate(coordinate, precision) for coordinate in self.coordinates])

    def __str__(self):
        return str(self.coordinates)

    def __eq__(self, other):
        return self.coordinates==other.coordinates
