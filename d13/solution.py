import math
import re

import numpy as np


def parse_input(sample=False):
    file = "./puzzle_input.txt"
    if sample:
        file = "./sample_input.txt"
    with open(file, "r") as f:
        input_text = f.read()

    pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\n"
        r"Button B: X\+(\d+), Y\+(\d+)\n"
        r"Prize: X=(\d+), Y=(\d+)"
    )

    results = []
    for match in pattern.finditer(input_text):
        button_a = [int(match.group(1)), int(match.group(2))]
        button_b = [int(match.group(3)), int(match.group(4))]
        prize = [int(match.group(5)), int(match.group(6))]
        results.append([button_a, button_b, prize])
    return results


def is_close_to_integer(value, tolerance=1e-5):
    return math.isclose(value, round(value), abs_tol=tolerance)


def solve():
    total = 0
    parsed_input = parse_input()
    for c in parsed_input:
        L = np.array([[c[0][0], c[1][0]], [c[0][1], c[1][1]]])
        R = np.array([c[2][0], c[2][1]])

        A, B = np.linalg.solve(L, R)
        print(f"A: {A}, B: {B}")

        if is_close_to_integer(A):
            A = round(A)

        if is_close_to_integer(B):
            B = round(B)

        if A.is_integer() and B.is_integer() and max(A, B) <= 100:
            total += 3 * A + B

    print(f"TOTAL: {total}")


if __name__ == "__main__":
    parsed_input = parse_input()
    print(f"INPUT: {parsed_input}")
    solve()
