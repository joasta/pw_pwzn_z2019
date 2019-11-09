"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie pola
figury na podstawie podanych parametrów. - bez tworzenia instancji, Circle.get_perimeter(3)
get_area, get_perimeter
- Zaimplementuj classmethod "name" zwracającą nazwę klasy. [w Figure]
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych. [w tym użyć are_diagonals_equal]
- Zwiąż ze sobą atrybuty e i f (w klasie Diamond) oraz a, b, e i f
(w klasie Square) [jak jedno przeskaluję, mają zmienić się oba]
"""
from numbers import Number
from math import pi, sqrt

class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area():.3f}, '
            f'perimeter={self.perimeter():.3f}'
        )

class Circle(Figure):
    __r = 1

    def __init__(self, r):
        self.r = r

    @property
    def r(self):
        return self.__r
    @r.setter
    def r(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self.__r = x

    def area(self):
        ar = pi * self.r * self.r
        return ar

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
    __a = 1.5
    __b = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.__a
    def set_a(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self.__a = x
    a = property(get_a, set_a)

    def get_b(self):
        return self.__b
    def set_b(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else: self.__b = x
    b = property(get_b, set_b)

    def area(self):
        ar = self.a * self.b
        return ar

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
    __e = 1
    __f = 1

    def __init__(self, a, b):
        self.__e = a
        self.__f = b

    def get_e(self):
        return self.__e
    def set_e(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            ratio = x/self.__e
            self.__e = x
            self.__f *= ratio
    e = property(get_e, set_e)

    def get_f(self):
        return self.__f
    def set_f(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            ratio = x/self.__e
            self.__f = x
            self.__e *= ratio
    f = property(get_f, set_f)

    def area(self):
        ar = self.e * self.f / 2
        return ar

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


class Square(Rectangle, Diamond, Figure):
    def __init__(self, a):
        self.a = a
        self.e = a*sqrt(2)
        
    def get_a(self):
        return self.__a
    def set_a(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self.__a = x
            self.__b = x
    a = property(get_a, set_a)
    
    def get_b(self):
        return self.__b
    def set_b(self, x):
        if not isinstance(x, Number):
            print("Not number value!")
        else:
            self.__b = x
            self.__a = x
    b = property(get_b, set_b)

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
    #assert str(diam_2) == 'Square: area=0.500, perimeter=2.828'
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'