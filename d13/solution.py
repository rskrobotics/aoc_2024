import re

import numpy as np

INPUT_FILE = "./puzzle_input.txt"
SAMPLE_INPUT_FILE = "./sample_input.txt"
OFFSET = 10_000_000_000_000


def parse_input(sample=False):
    file = SAMPLE_INPUT_FILE if sample else INPUT_FILE
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


def custom_round_two(A, B, lower_threshold=0.005, upper_threshold=0.995):
    def process_value(value):
        integer_part = int(value)
        fractional_part = abs(value - integer_part)

        if fractional_part <= lower_threshold:
            return integer_part, True
        elif fractional_part >= upper_threshold:
            rounded_value = integer_part + 1 if value > 0 else integer_part - 1
            return rounded_value, True
        else:
            return value, False

    rounded_A, success_A = process_value(A)
    rounded_B, success_B = process_value(B)

    ok = success_A and success_B

    print(f"A: {A} -> Rounded A: {rounded_A}")
    print(f"B: {B} -> Rounded B: {rounded_B}")
    print(f"Rounding Successful for A: {success_A}")
    print(f"Rounding Successful for B: {success_B}")
    print(f"Both Rounded Successfully: {ok}")

    return rounded_A, rounded_B, ok


def solve(parsed_input):
    total = 0
    for c in parsed_input:
        L = np.array([[c[0][0], c[1][0]], [c[0][1], c[1][1]]])
        R = np.array([c[2][0] + 10_000_000_000_000, c[2][1] + 10_000_000_000_000])
        A, B = np.linalg.solve(L, R)
        print(f"A: {A}, B: {B}")

        A, B, ok = custom_round_two(A, B)
        if ok:
            total += 3 * A + B

    print(f"TOTAL: {total}")


if __name__ == "__main__":
    parsed_input = parse_input()
    print(f"INPUT: {parsed_input}")
    solve(parsed_input)
