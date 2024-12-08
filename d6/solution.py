def parse_input():
    m = []
    with open("./puzzle_input.txt", "r") as f:
        for line in f:
            m.append(list(line.strip()))
    return m


def rotate(guard):
    directions = ["N", "E", "S", "W"]
    index = (directions.index(guard[2]) + 1) % 4
    guard[2] = directions[index]
    return guard


def execute_movement(m, guard):
    exited = False
    r, c = guard[0], guard[1]
    R, C = len(m), len(m[0])
    if (
        (guard[2] == "N" and r == 0)
        or (guard[2] == "W" and c == 0)
        or (guard[2] == "E" and c == C - 1)
        or (guard[2] == "S" and r == R - 1)
    ):
        m[r][c] = "X"
        exited = True
    else:
        if (
            (guard[2] == "N" and m[r - 1][c] == "#")
            or (guard[2] == "S" and m[r + 1][c] == "#")
            or (guard[2] == "E" and m[r][c + 1] == "#")
            or (guard[2] == "W" and m[r][c - 1] == "#")
        ):
            guard = rotate(guard)
        else:
            m[r][c] = "X"
            match guard[2]:
                case "N":
                    m[r - 1][c] = "^"
                    guard[0] -= 1
                case "S":
                    m[r + 1][c] = "^"
                    guard[0] += 1
                case "E":
                    m[r][c + 1] = "^"
                    guard[1] += 1
                case "W":
                    m[r][c - 1] = "^"
                    guard[1] -= 1
    return exited, m, guard


def solve_pt1():
    m = parse_input()
    exited = False
    guard = [-1, -1, "N"]
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == "^":
                guard[0] = r
                guard[1] = c
    print(f"Guard: {guard}")
    # print(f"m: {m}")
    while not exited:
        exited, m, guard = execute_movement(m, guard)

    pt1 = sum(v == "X" for r in m for v in r)
    print(f"PT1: {pt1}")


def modify_map(m, r, c):
    modified = False
    if m[r][c] != "^":
        m[r][c] = "#"
        modified = True
    return m, modified


def solve_pt2():
    count = 0
    m = parse_input()
    for r in range(len(m)):
        for c in range(len(m[0])):
            mm = [row[:] for row in m]
            mm, modified = modify_map(mm, r, c)
            if modified:
                visited = set()
                exited = False
                guard = [-1, -1, "N"]
                for r2 in range(len(mm)):
                    for c2 in range(len(mm[0])):
                        if mm[r2][c2] == "^":
                            guard[0] = r2
                            guard[1] = c2
                while not exited:
                    if tuple(guard) in visited:
                        print("Loop detected!")
                        count += 1
                        exited = True
                        break
                    visited.add(tuple(guard))
                    exited, mm, guard = execute_movement(mm, guard)

                print("Exited LOOP!")
    print(f"LOOPZ: {count}")


if __name__ == "__main__":
    solve_pt2()
