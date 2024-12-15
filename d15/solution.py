def parse_input(sample=False):
    fname = "./sample_input.txt" if sample else "./puzzle_input.txt"
    with open(fname, "r") as file:
        grid_part, instructions_part = file.read().strip().split("\n\n")
    grid = [list(line) for line in grid_part.splitlines()]
    instructions = instructions_part.replace("\n", "").strip()
    return grid, instructions


def calculate_gps(grid):
    total = sum(
        100 * r + c
        for r, row in enumerate(grid)
        for c, cell in enumerate(row)
        if cell == "O"
    )
    print(f"Total: {total}")


def print_grid(grid):
    print("\n".join("".join(row) for row in grid))
    print("\n" + "-" * 20 + "\n")


def solve():
    directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    grid, instructions = parse_input()

    robot = next(
        [r, c]
        for r, row in enumerate(grid)
        for c, cell in enumerate(row)
        if cell == "@"
    )

    print("Initial Grid State:")
    print_grid(grid)

    for i in instructions:
        dr, dc = directions[i]
        moves = 1
        while True:
            nr, nc = robot[0] + dr * moves, robot[1] + dc * moves
            if grid[nr][nc] == "O":
                moves += 1
            elif grid[nr][nc] == "#":
                break
            else:
                if moves > 1:
                    grid[nr][nc] = "O"
                grid[robot[0] + dr][robot[1] + dc], grid[robot[0]][robot[1]] = "@", "."
                robot[0], robot[1] = robot[0] + dr, robot[1] + dc
                print(f"After instruction '{i}':")
                print_grid(grid)
                break

    calculate_gps(grid)


if __name__ == "__main__":
    solve()

