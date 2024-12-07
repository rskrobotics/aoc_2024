def solve_pt1():
    puzzle = []
    x = "XMAS"
    with open("./puzzle_input.txt", "r") as input_file:
        for line in input_file:
            puzzle.append(line.strip("\n"))

    ROWS, COLS = len(puzzle), len(puzzle[0])

    def checker(r, c):
        if puzzle[r][c] != "X":
            return 0

        # Check right
        right = c <= COLS - 4 and puzzle[r][c : c + 4] == x

        # Check left
        left = c >= 3 and puzzle[r][c - 3 : c + 1] == x[::-1]

        # Check up
        up = r >= 3 and "".join(puzzle[r - i][c] for i in range(4)) == x

        # Check down
        down = r <= ROWS - 4 and "".join(puzzle[r + i][c] for i in range(4)) == x

        # Check up-right
        up_right = (
            r >= 3
            and c <= COLS - 4
            and "".join(puzzle[r - i][c + i] for i in range(4)) == x
        )

        # Check up-left
        up_left = (
            r >= 3 and c >= 3 and "".join(puzzle[r - i][c - i] for i in range(4)) == x
        )

        # Check down-right
        down_right = (
            r <= ROWS - 4
            and c <= COLS - 4
            and "".join(puzzle[r + i][c + i] for i in range(4)) == x
        )

        # Check down-left
        down_left = (
            r <= ROWS - 4
            and c >= 3
            and "".join(puzzle[r + i][c - i] for i in range(4)) == x
        )

        return sum([right, left, up, down, up_right, up_left, down_right, down_left])

    total_sum = sum(checker(r, c) for r in range(ROWS) for c in range(COLS))
    print(f"SUM: {total_sum}")


if __name__ == "__main__":
    solve_pt1()
