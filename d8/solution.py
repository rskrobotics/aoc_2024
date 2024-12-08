import operator
import re
from collections import defaultdict
from itertools import combinations


def parse_file():
    data = []
    with open("./puzzle_input.txt", "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def is_within_bounds(r_max: int, c_max, coords: tuple[int, int]):
    if coords[0] < 0 or coords[0] >= r_max or coords[1] < 0 or coords[1] >= r_max:
        return False
    return True


def get_antinode_coords(
    n1: tuple[int, int], n2: tuple[int, int], row_max: int, col_max: int
) -> set(tuple[int, int]):
    antinodes = set()
    vector = tuple(map(operator.sub, n1, n2))
    added = tuple(map(operator.add, n1, vector))
    substracted = tuple(map(operator.sub, n2, vector))
    if is_within_bounds(row_max, col_max, added):
        antinodes.add(added)

    if is_within_bounds(row_max, col_max, substracted):
        antinodes.add(substracted)

    # print(f"NODES: {n1}, {n2}, ANTINODES: {antinodes}")

    return antinodes


def solve_pt1():
    data = parse_file()
    antennas = defaultdict(set)
    pattern = re.compile(r"\w")
    for row, line in enumerate(data):
        matches = re.finditer(pattern, line)
        for match in matches:
            col = match.start()
            frequency = match.group()
            antennas[frequency].add((row, col))
    # print(f"ANTENNAS: {antennas}")

    antinodes = defaultdict(set)
    for frequency, coords in antennas.items():
        pairs = list(combinations(coords, 2))
        antinodes[frequency] = set.union(
            *[get_antinode_coords(*pair, len(data), len(data[0])) for pair in pairs]
        )

    print(f"Solution: {len(set.union(*[v for v in antinodes.values()]))}")


if __name__ == "__main__":
    # data = parse_file()
    # print(f"parse_file: {data}")
    solve_pt1()
    # get_antinode_coords((10, 10), (15, 15), 100, 100)
