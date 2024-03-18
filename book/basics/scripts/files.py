#!/usr/bin/python3
import json
import yaml
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


def from_file(path):
    if path.endswith(".yml"):
        return from_yaml(path)
    if path.endswith(".json"):
        return from_json(path)
    # else - вызываем стандартное исключение (ошибку)
    raise ValueError("unused file format")


def from_yaml(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data["a"], data["b"], data["c"]


def from_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data["a"], data["b"], data["c"]


if __name__ == "__main__":
    parser = ArgumentParser(
        "solve_quadric_eq",
        description="Let you solve any quadric equation a*x^2 + b*x + c = 0"
    )
    parser.add_argument(
        "-l",
        "--line",
        dest="line",
        type=float,
        nargs="?",
        help="Input coefficients using command line"
    )
    parser.add_argument(
        "-a",
        type=float,
        default=1,
        help="The `a` coefficient (default 1)"
    )
    parser.add_argument(
        "-b",
        type=float,
        default=0,
        help="The `b` coefficient (default 0)"
    )
    parser.add_argument(
        "-c",
        type=float,
        default=0,
        help="The `c` coefficient (default 0)"
    )
    parser.add_argument(
        "-f",
        "--from-file",
        dest="file_path",
        help="Read coefficients from the data file (JSON or YAML)"
    )
    
    args = parser.parse_args()
    if args.file_path is not None:
        a, b, c = from_file(args.file_path)
    elif "line" in args:
        a = args.a
        b = args.b
        c = args.c
    else:
        raise ValueError("unknown command line format")
    x1, x2 = solve(a, b, c)
    print("x1 =", x1)
    print("x2 =", x2)
