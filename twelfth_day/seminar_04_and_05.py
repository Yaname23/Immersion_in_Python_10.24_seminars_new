"""
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.

"""

"""
Задание №5
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.

"""
class Rectangle:
    __slots__= ['width', 'height']


    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self.width + self._height)

    def area(self):
        return self.width * self.height


    def __str__(self):
        return f'Прямоугольник со сторонами {self.width}, height={self.height}'

    def __repr__(self):
        return f'Прямоугольник({self.width}, {self.height})'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('так нельзя')
        self._width = value
    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('так нельзя')
        self._height = value

r1 = Rectangle(1, 2)
r1.width = -1