from collections import defaultdict

directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]


def parse_input():
    data = []
    with open("./puzzle_input.txt", "r") as f:
        for line in f:
            data.append(list(line.strip()))

    return data


def parse_sample_input():
    data = []
    with open("./example.txt", "r") as f:
        for line in f:
            data.append(list(line.strip()))

    print(f"DATA: {data}")
    return data


def get_neighbours(data, coord):
    rows, cols = len(data), len(data[0])
    r, c = coord

    return [
        int(data[r + dr][c + dc]) if 0 <= r + dr < rows and 0 <= c + dc < cols else None
        for dr, dc in directions
    ]


def traverse_down(data, coord, m, initiator):
    r, c = coord
    cval = int(data[r][c])
    if cval == 0:
        m[coord].add(initiator)
        print(f"Incrementing {coord}")
        return
    ngh = get_neighbours(data, coord)

    for n, dir in zip(ngh, directions):
        if n is not None and n == cval - 1:
            traverse_down(data, (r + dir[0], c + dir[1]), m, initiator)


def traverse_peaks(data, nines, m):
    for coord in nines:
        traverse_down(data, coord, m, coord)


def solve():
    m = defaultdict(set)
    # data = parse_sample_input()
    data = parse_input()
    zeros, nines = [], []

    [
        zeros.append((i, j)) if int(cell) == 0 else nines.append((i, j))
        for i, row in enumerate(data)
        for j, cell in enumerate(row)
        if int(cell) == 0 or int(cell) == 9
    ]
    traverse_peaks(data, nines, m)
    total = 0
    for k, v in m.items():
        print(f"k, v: {k}, {v}")
        total += len(v)
    print(f"TOTAL: {total}")

    print(f"ZEROS: {zeros}")
    print(f"NINES: {nines}")


if __name__ == "__main__":
    # data = parse_input()
    # print(f"Data: {data}")
    solve()
