#!/usr/bin/python3

# Импортируем
from argparse import ArgumentParser
from cmath import sqrt as csqrt
from math import sqrt


def solve(a, b, c):
    discriminant = b*b - 4*a*c
    if discriminant >= 0:
        return (
            (-b - sqrt(discriminant)) / (2*a),
            (-b + sqrt(discriminant)) / (2*a)
        )
    return (
        (-b - csqrt(complex(discriminant))) / (2*a),
        (-b + csqrt(complex(discriminant))) / (2*a)
    )


# Ещё одно важное изменение -
# мы выделяем код, с которого начинается выполнение
# скрипта при его вызове
if __name__ == "__main__":
    # Получаем коэффициенты из командной строки
    parser = ArgumentParser(
        "solve_quadric_eq",
        description="Let you solve any quadric equation a*x^2 + b*x + c = 0"
    )
    parser.add_argument(
        "a",
        type=float,
        help="The first coefficient of the equation"
    )
    parser.add_argument(
        "b",
        nargs="?",
        type=float,
        default=0,
        help="The second coefficient of the equation (default 0)"
    )
    parser.add_argument(
        "c",
        nargs="?",
        type=float,
        default=0,
        help="The third coefficient of the equation (default 0)"
    )
    parser.add_argument(
        "-B",
        type=float,
        help="The second coefficient of the equation (default 0)"
    )
    parser.add_argument(
        "-C",
        type=float,
        help="The third coefficient of the equation (default 0)"
    )

    args = parser.parse_args()
    a, b, c = args.a, args.b, args.c
    if args.B is not None:
        b = args.B
    if args.C is not None:
        c = args.C
    # Решение
    x1, x2 = solve(a, b, c)
    # Вывод на экран
    print("x1 =", x1)
    print("x2 =", x2)