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

    print(sum(abs(b - a) for a, b in zip(left, right)))
    print(sum(a * right.count(a) for a in left))


if __name__ == "__main__":
    solve()
