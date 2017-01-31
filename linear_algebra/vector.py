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
    def __str__(self):
        return str(self.coordinates)
    def __eq__(self, other):
        return self.coordinates==other.coordinates
