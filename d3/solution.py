import re


def solve_pt1():
    total = 0
    with open("./puzzle_input.txt", "r") as input:
        for a, b in re.findall(r"mul\((\d+),(\d+)\)", input.read()):
            total += int(a) * int(b)
    print(f"Total: {total}")


def solve_pt2():
    total = 0
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"
    mul_regex = r"mul\((\d+),(\d+)\)"

    enable_flag = True
    with open("./puzzle_input.txt", "r") as input:
        for pattern in re.finditer(
            f"{do_regex}|{dont_regex}|{mul_regex}", input.read()
        ):
            if re.fullmatch(do_regex, pattern.group()):
                enable_flag = True
            elif re.fullmatch(dont_regex, pattern.group()):
                enable_flag = False
            elif enable_flag:
                total += int(pattern.group(1)) * int(pattern.group(2))

    print(f"Total: {total}")


if __name__ == "__main__":
    solve_pt1()
    solve_pt2()
