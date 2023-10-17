from datetime import datetime

from .models import DestinyMatrixContent


class DestinyMatrix:

    class Points:
        __slots__ = (
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'y', 'k', 'a1', 'a2', 'd1', 'd2',
            'h', 'j', 'm', 'n', 't', 'z', 's', 'c1', 'x', 'x2', 'x1', 'c2', 'e1',
            'e2', 'p1', 'p2', 's1', 's2', 'l', 'b1', 'b2', 'b3', 'l1', 'l2', 'l3',
            'l4', 'l5', 'l6', 'a3'
        )

        def __init__(self):
            for slot in self.__slots__:
                setattr(self, slot, 0)

        def __setattr__(self, key, value):
            # TODO: Насколько это все круто, если это малочитаемо?? (можно было просто сумму оставить)
            if isinstance(value, tuple):
                point = sum(value)
            else:
                point = value
            while point > 22:
                point = sum(map(int, str(point)))
            super().__setattr__(key, point)

        def to_dict(self):
            return {slot: getattr(self, slot) for slot in self.__slots__}

        def __str__(self):
            return '\n'.join([f'{key}: {value}' for key, value in self.to_dict().items()])

    def __init__(self, date: datetime):
        self.date = date
        self.points = self.Points()

    def __get_birth_numbers(self) -> list[int]:
        """
        :return: list; example [16, 4, 1998]
        """
        return [self.date.day, self.date.month, self.date.year]

    def __add_points_first_group(self):
        """
        points a, b, c, d, e
        """
        day, month, year = self.__get_birth_numbers()
        self.points.a = day
        self.points.b = month
        self.points.c = year
        self.points.d = tuple(self.points.to_dict().values())
        self.points.e = tuple(self.points.to_dict().values())

    def __add_points_second_group(self):
        """
        points f, g, y, k
        """
        self.points.f = (self.points.a, self.points.b)
        self.points.g = (self.points.b, self.points.c)
        self.points.y = (self.points.c, self.points.d)
        self.points.k = (self.points.a, self.points.d)

    def __add_points_third_group(self):
        """
        points a1, a2, d1, d2
        """
        self.points.a1 = (self.points.a, self.points.e)
        self.points.a2 = (self.points.a, self.points.a1)
        self.points.d1 = (self.points.d, self.points.e)
        self.points.d2 = (self.points.d, self.points.d1)

    def __add_points_fourth_group(self):
        """
        points h, j, m, n, t, z, s
        """
        self.points.h = (self.points.b, self.points.d)
        self.points.j = (self.points.a, self.points.c)
        self.points.m = (self.points.h, self.points.j)
        self.points.n = (self.points.f, self.points.y)
        self.points.t = (self.points.g, self.points.k)
        self.points.z = (self.points.n, self.points.t)
        self.points.s = (self.points.m, self.points.z)

    def __add_points_fifth_group(self):
        """
        points c1, x, x1, x2, c2
        """
        self.points.c1 = (self.points.c, self.points.e)
        self.points.x = (self.points.d1, self.points.c1)
        self.points.x2 = (self.points.x, self.points.c1)
        self.points.x1 = (self.points.d1, self.points.x)
        self.points.c2 = (self.points.c, self.points.c1)

    def __add_points_sixth_group(self):
        """
        points e1, e2, p1, p2, s1, s2
        """
        # TODO: add s3, s4, o calculations
        self.points.e1 = (self.points.f, self.points.g, self.points.y, self.points.k)
        self.points.e2 = (self.points.e, self.points.e1)
        self.points.p1 = (self.points.g, self.points.e1)
        self.points.p2 = (self.points.g, self.points.p1)
        self.points.s1 = (self.points.f, self.points.e1)
        self.points.s2 = (self.points.f, self.points.s1)

    def __add_points_seventh_group(self):
        """
        points l, b1, b2, b3, l1, l2, l3, l4, l5, l6, a3
        """
        self.points.l = (self.points.a, self.points.b)
        self.points.b1 = (self.points.b, self.points.e)
        self.points.b2 = (self.points.b, self.points.b1)
        self.points.b3 = (self.points.b1, self.points.e)
        self.points.l1 = (self.points.a2, self.points.b2)
        self.points.l2 = (self.points.a1, self.points.b1)
        self.points.l3 = (self.points.a3, self.points.b3)
        self.points.l4 = (self.points.e, self.points.e)
        self.points.l5 = (self.points.d1, self.points.c1)
        self.points.l6 = (self.points.d, self.points.c)
        self.points.a3 = (self.points.a1, self.points.e)

    def get_matrix_points(self):
        self.__add_points_first_group()
        self.__add_points_second_group()
        self.__add_points_third_group()
        self.__add_points_fourth_group()
        self.__add_points_fifth_group()
        self.__add_points_sixth_group()
        self.__add_points_seventh_group()
        # return self.points

    def get_matrix_points_w_titles(self):
        return {
            'Визитная карточка': [f'{self.points.a}', ],
            'Поддержка высших сил': [f'{self.points.b}', ],
            'Жизненный путь, главная проработка души': [f'{self.points.c}', ],
            'Карма прошлого воплощения': [f'{self.points.d}', ],
            'Зона комфорта': [f'{self.points.e}', ],
            # 'Родовые программы': [f'{self.points.f}-{self.points.s2}-{self.points.s1}',
            #                       f'{self.points.g}-{self.points.p2}-{self.points.p1}', ]
        }


def get_contents(matrix_codes) -> list:
    """
    Returns list with DestinyMatrixContent objects
    for current calculation.
    """
    response: list = []
    for title, values in matrix_codes.items():
        response.extend(
            DestinyMatrixContent.objects.filter(
                title=title,
                code__in=values
            )
        )
    return response
