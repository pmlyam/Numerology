from dataclasses import dataclass
from datetime import datetime


class dict_as_obj(dict):

    def __getattr__(self, name):
        return self.get(name)

    def __setattr__(self, name, value):
        self[name] = value


class Calculator:

    def __init__(self, date: datetime):
        self.date = date

    def __get_birth_numbers(self) -> list[int]:
        """
        :return: list; example [16, 4, 1998]
        """
        return [self.date.day, self.date.month, self.date.year]

    def __get_birth_additional_numbers(self) -> list[int]:
        """
        :return: list; example [38, 11, 36, 9]
        """
        date_to_string = "".join(str(n) for n in self.__get_birth_numbers())
        first_numbers = sum(map(int, date_to_string))
        second_numbers = (
            first_numbers if first_numbers < 13
            else sum(map(int, str(first_numbers)))
        )
        third_numbers = (
            first_numbers - (2 * int(str(self.date.day)[0]))
            if self.date.year < 2000 else first_numbers + 19
        )
        fourth_numbers = (
            third_numbers if third_numbers < 13
            else sum(map(int, str(third_numbers)))
        )
        return [first_numbers, second_numbers, third_numbers, fourth_numbers]

    def __get_all_birth_numbers(self) -> list[int]:
        """
        :return: list; example [16, 4, 1998, 38, 11, 36, 9]
        """
        return self.__get_birth_numbers() + self.__get_birth_additional_numbers()

    def get_numbers(self) -> list[str]:
        """
        :return: list; example ['1111', '-', '33', '4', '-', '66', '-', '88', '999']
        """
        numbers = str(self.__get_all_birth_numbers())
        square_numbers = [
            ''.join(
                str(num) for _ in range(0, numbers.count(str(num)))
            ) if str(num) in numbers else '-' for num in range(1, 10)
        ]
        return square_numbers

    def get_additional_numbers(self) -> list[str]:
        """
        :return: list; example ['6', '3', '5', '2', '5', '2', '7', '7']
        """
        basic_numbers = self.get_numbers()

        def calculate(index: tuple):
            num = len((basic_numbers[index[0]] +
                       basic_numbers[index[1]] +
                       basic_numbers[index[2]]
                       ).replace('-', ''))
            return str(num) if num > 0 else '-'
        return [calculate((0, 1, 2)), calculate((3, 4, 5)), calculate((6, 7, 8)),
                calculate((2, 4, 6)), calculate((0, 3, 6)),
                calculate((1, 4, 7)), calculate((2, 5, 8)), calculate((0, 4, 8))]

    def get_all_numbers(self) -> list[str]:
        """
        :return: list; example
        ['1111', '-', '33', '4', '-', '66', '-', '88', '999', '6', '3', '5', '2', '5', '2', '7', '7']
        """
        return self.get_numbers() + self.get_additional_numbers()


class CalculatorMatrix:
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

    def add_points_first_group(self):
        """
        points a, b, c, d, e
        """
        day, month, year = self.__get_birth_numbers()
        self.points.a = day
        self.points.b = month
        self.points.c = year
        self.points.d = tuple(self.points.to_dict().values())
        self.points.e = tuple(self.points.to_dict().values())

    def add_points_second_group(self):
        """
        points f, g, y, k
        """
        self.points.f = (self.points.a, self.points.b)
        self.points.g = (self.points.b, self.points.c)
        self.points.y = (self.points.c, self.points.d)
        self.points.k = (self.points.a, self.points.d)

    def add_points_third_group(self):
        """
        points a1, a2, d1, d2
        """
        self.points.a1 = (self.points.a, self.points.e)
        self.points.a2 = (self.points.a, self.points.a1)
        self.points.d1 = (self.points.d, self.points.e)
        self.points.d2 = (self.points.d, self.points.d1)

    def add_points_fourth_group(self):
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

    def add_points_fifth_group(self):
        """
        points c1, x, x1, x2, c2
        """
        self.points.c1 = (self.points.c, self.points.e)
        self.points.x = (self.points.d1, self.points.c1)
        self.points.x2 = (self.points.x, self.points.c1)
        self.points.x1 = (self.points.d1, self.points.x)
        self.points.c2 = (self.points.c, self.points.c1)

    def add_points_sixth_group(self):
        """
        points e1, e2, p1, p2, s1, s2
        """
        self.points.e1 = (self.points.f, self.points.g, self.points.y, self.points.k)
        self.points.e2 = (self.points.e, self.points.e1)
        self.points.p1 = (self.points.g, self.points.e1)
        self.points.p2 = (self.points.g, self.points.p1)
        self.points.s1 = (self.points.f, self.points.e1)
        self.points.s2 = (self.points.f, self.points.s1)

    def add_points_seventh_group(self):
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
        self.add_points_first_group()
        self.add_points_second_group()
        self.add_points_third_group()
        self.add_points_fourth_group()
        self.add_points_fifth_group()
        self.add_points_sixth_group()
        self.add_points_seventh_group()
        return self.points


date = datetime(1986, 11, 21)

calculator = CalculatorMatrix(date)
print(calculator.get_matrix_points())
