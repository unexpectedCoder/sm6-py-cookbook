#!/usr/bin/python3

# Импортируем
import sys

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
    args = sys.argv
    a, b, c = float(args[1]), float(args[2]), float(args[3])
    # Решение
    x1, x2 = solve(a, b, c)
    # Вывод на экран
    print("x1 =", x1)
    print("x2 =", x2)
