from collections import deque
from itertools import product


def parse_input(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


def propagate(data):
    directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    rows, cols = len(data), len(data[0])
    visited = [[False] * cols for _ in range(rows)]
    groups = []

    def dfs(r, c, letter):
        stack, group = [(r, c)], []
        while stack:
            r, c = stack.pop()
            if (
                0 <= r < rows
                and 0 <= c < cols
                and not visited[r][c]
                and data[r][c] == letter
            ):
                visited[r][c] = True
                group.append((r, c))
                stack.extend((r + dr, c + dc) for dr, dc in directions)
        return group

    def calculate_sides(group):
        group_set = set(group)

        directions = {"L": (0, -1), "D": (1, 0), "U": (-1, 0), "R": (0, 1)}

        edges = {"L": [], "D": [], "U": [], "R": []}

        for r, c in group:
            for direction, (dr, dc) in directions.items():
                if (r + dr, c + dc) not in group_set:
                    edges[direction].append((r, c))

        def group_continuous_segments(cells):
            seen = set()
            segments = 0

            def bfs(start):
                queue = deque([start])
                seen.add(start)
                while queue:
                    current = queue.popleft()
                    for neighbor in [
                        (current[0] + 1, current[1]),
                        (current[0] - 1, current[1]),
                        (current[0], current[1] + 1),
                        (current[0], current[1] - 1),
                    ]:
                        if neighbor in cells and neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)

            for cell in cells:
                if cell not in seen:
                    bfs(cell)
                    segments += 1

            return segments

        sides_count = sum(
            group_continuous_segments(edges[direction]) for direction in edges
        )

        print(f"L: {edges['L']}")
        print(f"D: {edges['D']}")
        print(f"U: {edges['U']}")
        print(f"R: {edges['R']}")
        print(f"Total sides: {sides_count}")
        return sides_count

    def calculate_perimeter(group):
        return sum(
            1
            for r, c in group
            for dr, dc in directions
            if not (
                0 <= r + dr < rows
                and 0 <= c + dc < cols
                and data[r + dr][c + dc] == data[r][c]
            )
        )

    for r, c in product(range(rows), range(cols)):
        if not visited[r][c]:
            group = dfs(r, c, data[r][c])
            sides = calculate_sides(group)
            groups.append((data[r][c], group, calculate_perimeter(group), sides))

    return groups


def solve():
    data = parse_input("./puzzle_input.txt")
    groups = propagate(data)
    total = sum(perimeter * len(group) for _, group, perimeter, _ in groups)
    total_2 = sum(sides * len(group) for _, group, _, sides in groups)
    print(f"Total: {total}")
    print(f"Total: {total_2}")


if __name__ == "__main__":
    solve()
