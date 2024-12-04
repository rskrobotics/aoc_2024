def solve():
    with open("./puzzle_input.txt", "r") as input:
        left, right = [], []
        for line in input:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

    # print(f"Left: {left}")
    # print(f"Right: {right}")
    left.sort()
    right.sort()

    return sum(abs(b - a) for a, b in zip(left, right))


if __name__ == "__main__":
    print(f"{solve()}")
