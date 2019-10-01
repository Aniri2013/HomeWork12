import math
class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        print('Создание сферы ', self.__class__.__name__)
        self.__r = r
        self.__x = x
        self.__y = y
        self.__z = z
    def get_volume(self):
        print('Вычисление объема')
        return '{0:.5f}'.format(4 / 3 * math.pi * math.pow(self.__r, 3))
    def get_square(self):
        print('Вычисление площади')
        return '%.5f' % (4 * math.pi * math.pow(self.__r, 2))
    def get_radius(self):
        print('Получение радиуса')
        return self.__r
    def get_center(self):
        print('Получение координат центра сферы')
        return tuple((self.__x, self.__y, self.__z))
    def set_radius(self, r):
        print('Новый радиус: ', r)
        self.__r = r
    def set_center(self, x, y, z):
        print('Новый центр: x = {}, y = {}, z = {}'.format(x, y, z))
        self.__x = x
        self.__y = y
        self.__z = z
    def is_point_inside(self, x, y, z):
        a = 'Принадлежность точки ({}, {}, {}) сфере: '.format(x, y, z)
        return (a + str(math.pow((self.__x - x), 2) +
                        math.pow((self.__y - y), 2) +
                        math.pow((self.__z - z), 2) <= math.pow(self.__r, 2)))
sphere1 = Sphere()
print('Сфера создана без параметров')
print('Объем сферы 1:', sphere1.get_volume())
print('Радиус сферы 1:', sphere1.get_radius())
print('Центр сферы 1:', sphere1.get_center())
print()
sphere2 = Sphere(5)
print('Сфера 2 создана, задан только радиус')
print('Объем сферы 2:', sphere2.get_volume())
print('Радиус сферы 2:', sphere2.get_radius())
print('Центр сферы 2:', sphere2.get_center())
print()
sphere3 = Sphere(6, 10.5, 14.3, -3.2)
print('Сфера 3 создана со всеми параметрами')
print('Объем сферы 3:', sphere3.get_volume())
print('Площадь сферы 3:', sphere3.get_square())
print('Радиус сферы 3:', sphere3.get_radius())
print('Центр сферы 3:', sphere3.get_center())
sphere3.set_radius(7)
print('Радиус сферы 3:', sphere3.get_radius())
sphere3.set_center(5, 5, 5)
print('Центр сферы 3:', sphere3.get_center())
print(sphere3.is_point_inside(6, 6, 6))
print(sphere3.is_point_inside(0, 1, 3))
print(sphere3.is_point_inside(0, 0, 0))