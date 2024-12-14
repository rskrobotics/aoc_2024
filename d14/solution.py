import re


def sum_quadrants(board):
    mid_row, mid_col = len(board) // 2, len(board[0]) // 2

    top_left = sum(board[i][j] for i in range(mid_row) for j in range(mid_col))
    top_right = sum(
        board[i][j] for i in range(mid_row) for j in range(mid_col + 1, len(board[0]))
    )
    bottom_left = sum(
        board[i][j] for i in range(mid_row + 1, len(board)) for j in range(mid_col)
    )
    bottom_right = sum(
        board[i][j]
        for i in range(mid_row + 1, len(board))
        for j in range(mid_col + 1, len(board[0]))
    )

    return top_left * top_right * bottom_left * bottom_right


def parse_input():
    parsed_data = []
    with open("./puzzle_input.txt", "r") as f:
        pattern = re.compile(r"-?\d+")
        for line in f:
            numbers = list(map(int, pattern.findall(line)))
            print(f"NUMBERS: {numbers}")
            parsed_data.append(numbers)

    return parsed_data


def solve():
    data = parse_input()
    R, C = 103, 101
    board = [[0 for _ in range(C)] for _ in range(R)]
    for e in data:
        c = (e[0] + 100 * e[2]) % C
        r = (e[1] + 100 * e[3]) % R
        board[r][c] += 1

    print(f"sum_quadrants: {sum_quadrants(board)}")


if __name__ == "__main__":
    solve()
