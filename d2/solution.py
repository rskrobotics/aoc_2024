from itertools import pairwise


def solve():
    safe = 0
    with open("./puzzle_input.txt", "r") as input:
        for line in input:
            report = list(map(int, line.split()))
            is_increasing = all(a < b for a, b in pairwise(report))
            is_decreasing = all(a > b for a, b in pairwise(report))
            is_difference_valid = all(abs(b - a) <= 3 for a, b in pairwise(report))

            result = (is_increasing or is_decreasing) and is_difference_valid
            # print(f"{result}")
            if result:
                safe += 1
    print(f"Safe: {safe}")


def is_safe(report):
    is_increasing = all(a < b for a, b in pairwise(report))
    is_decreasing = all(a > b for a, b in pairwise(report))
    is_difference_valid = all(abs(b - a) <= 3 for a, b in pairwise(report))

    result = (is_increasing or is_decreasing) and is_difference_valid

    return result


def solve_pt_2():
    safe = 0
    with open("./puzzle_input.txt", "r") as input:
        for line in input:
            report = list(map(int, line.split()))

            safe += is_safe(report) or any(
                is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
            )
    print(f"Safe with_dampening: {safe}")


if __name__ == "__main__":
    solve()
    solve_pt_2()
