"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""
from numbers import Number
from math import pi, sqrt

class Figure:
    @property
    def area(self):
        raise NotImplementedError
    
    @property
    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):
    __r = 1

    def __init__(self, r):
        self.r = r

    @property
    def r(self):
        return self._r
    @r.setter
    def r(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self._r = x

    @property
    def area(self):
        ar = pi * self.r * self.r
        return ar

    @property
    def perimeter(self):
        per = 2 * pi * self.r
        return per

    @staticmethod
    def get_area(radius):
        return pi * radius * radius

    @staticmethod
    def get_perimeter(radius):
        return 2* pi * radius

class Rectangle(Figure):
    _a = 1.5
    _b = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self._a
    def set_a(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self._a = x
    a = property(get_a, set_a)

    def get_b(self):
        return self._b
    def set_b(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self._b = x
    b = property(get_b, set_b)
    
    @property
    def area(self):
        ar = self.a * self.b
        return ar
    
    @property
    def perimeter(self):
        per = 2 * (self.a + self.b)
        return per

    @staticmethod
    def get_area(a, b):
        return a * b

    @staticmethod
    def get_perimeter(a, b):
        return 2* (a + b)

class Diamond(Figure):
    _e = 1
    _f = 1

    def __init__(self, a, b):
        self._e = a
        self._f = b

    def get_e(self):
        return self._e
    def set_e(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._e = x
    e = property(get_e, set_e)

    def get_f(self):
        return self._f
    def set_f(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._f = x
    f = property(get_f, set_f)

    @property
    def area(self):
        ar = self.e * self.f / 2
        return ar
    
    @property
    def perimeter(self):
        per = 4 * sqrt((self.e*self.e+self.f*self.f)/4)
        return per

    @staticmethod
    def get_area(e,f):
        return e * f / 2

    @staticmethod
    def get_perimeter(e,f):
        return 4 * sqrt((e*e+f*f)/4)

    def are_diagonals_equal(self):
        if self.e==self.f:
            return True
        else: return False

    def to_square(self):

        if self.are_diagonals_equal():
            side = self.e / sqrt(2)
            return Square(side)
        else:
            print("Not a square!")
            return None


class Square(Rectangle, Diamond):
    def __init__(self, a):
        self.a = a
        self.e = a*sqrt(2)
        
    def set_a(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._a = x
            self._b = x
    a = property(Rectangle.get_a, set_a)
    
    def set_b(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._b = x
            self._a = x
    b = property(Rectangle.get_b, set_b)

    def set_e(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._e = x
            self._f = x
    e = property(Diamond.get_e, set_e)

    def set_f(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self._f = x
            self._e = x
    f = property(Diamond.get_f, set_f)

    @staticmethod
    def get_area(a):
        return a * a

    @staticmethod
    def get_perimeter(a):
        return 4*a


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'