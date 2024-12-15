import re
from statistics import stdev

import matplotlib.pyplot as plt
import numpy as np


def sum_quadrants(board):
    mid_row, mid_col = len(board) // 2, len(board[0]) // 2
    top_left = np.sum(board[:mid_row, :mid_col])
    top_right = np.sum(board[:mid_row, mid_col + 1 :])
    bottom_left = np.sum(board[mid_row + 1 :, :mid_col])
    bottom_right = np.sum(board[mid_row + 1 :, mid_col + 1 :])
    return top_left * top_right * bottom_left * bottom_right


def parse_input():
    parsed_data = []
    with open("./puzzle_input.txt", "r") as f:
        pattern = re.compile(r"-?\d+")
        for line in f:
            numbers = list(map(int, pattern.findall(line)))
            parsed_data.append(numbers)
    return parsed_data


def solve():
    iterations = 10_000
    data = parse_input()
    R, C = 103, 101
    board = np.zeros((R, C), dtype=int)

    cluster_measures = []

    for it in range(1, iterations + 1):
        board[:] = 0
        xs = []
        ys = []

        for e in data:
            c = (e[0] + it * e[2]) % C
            r = (e[1] + it * e[3]) % R
            board[r, c] = 1
            xs.append(c)
            ys.append(r)

        x_std = stdev(xs)
        y_std = stdev(ys)
        cluster_measures.append((it, x_std * y_std))

    best_iter, best_measure = min(cluster_measures, key=lambda x: x[1])

    board[:] = 0
    for e in data:
        c = (e[0] + best_iter * e[2]) % C
        r = (e[1] + best_iter * e[3]) % R
        board[r, c] = 1

    sq = sum_quadrants(board)
    print(f"Best clustering at iteration {best_iter} with measure {best_measure:.4f}")
    print(f"sum_quadrants at that iteration: {sq}")

    plt.imshow(board, cmap="viridis", interpolation="nearest")
    plt.title(f"Board at iteration {best_iter}")
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    solve()
