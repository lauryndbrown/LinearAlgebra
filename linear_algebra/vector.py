import collections
from decimal import Decimal
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
        products = tuple([float(Decimal(str(coordinate))*Decimal(str(scalar))) for coordinate in self.coordinates ])
        return Vector(products)

    def round_coordinates(self, num_decimals):
        self.coordinates = tuple([round(coordinate, num_decimals) for coordinate in self.coordinates])
    def __str__(self):
        return str(self.coordinates)
    def __eq__(self, other):
        return self.coordinates==other.coordinates
