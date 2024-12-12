from pprint import pprint


def parse_input():
    data = []
    with open("./puzzle_input.txt", "r") as f:
        for line in f:
            data.append(list(line.strip()))

    return data


def parse_sample_input():
    data = []
    with open("./sample_input.txt", "r") as f:
        for line in f:
            data.append(list(line.strip()))

    print(f"DATA: {data}")
    return data


def propagate(data):
    rows, cols = len(data), len(data[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    groups = []

    def dfs(r, c, letter, group):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or data[r][c] != letter:
            return

        visited[r][c] = True

        group.append((r, c))

        # LDUR
        dfs(r, c - 1, letter, group)
        dfs(r + 1, c, letter, group)
        dfs(r - 1, c, letter, group)
        dfs(r, c + 1, letter, group)

    def calculate_perimeter(group):
        perimeter = 0
        directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
        for r, c in group:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0
                    or nr >= rows
                    or nc < 0
                    or nc >= cols
                    or data[nr][nc] != data[r][c]
                ):
                    perimeter += 1
        return perimeter

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = data[r][c]
                group = []
                dfs(r, c, letter, group)
                perimeter = calculate_perimeter(group)
                groups.append((letter, group, perimeter))
    return groups


def solve():
    data = parse_input()
    groups = propagate(data)
    pprint(f"Groups: {groups}")
    total = sum(perimeter * len(group) for _, group, perimeter in groups)
    print(f"Total: {total}")


if __name__ == "__main__":
    solve()
