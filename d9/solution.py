def parse_input():
    with open("./puzzle_input.txt", "r") as f:
        input = f.read().strip()
    return input


def parse_sample_input():
    with open("./puzzle_input.txt", "r") as f:
        data = f.read().strip()

        cells = []
        datas = []
        empty = []
        pos = 0

        for i, d in enumerate(data, 1):
            cells += [
                i // 2 + 1 if i % 2 else 0,
            ] * int(d)

            if i % 2:
                datas.append([i // 2 + 1, int(d), pos])
            else:
                empty.append([0, int(d), pos])

            pos += int(d)

    return cells, datas, empty


def unfurl_input(data):
    disk = []
    current_file_number = 0
    is_file = True

    for length in data:
        disk.extend([current_file_number if is_file else "."] * int(length))
        if is_file:
            current_file_number += 1
        is_file = not is_file

    return disk


def swapper(disk):
    l, r = 0, len(disk) - 1
    while l < r:
        while disk[l] != ".":
            l += 1
        while disk[r] == ".":
            r -= 1
        disk[l], disk[r] = disk[r], disk[l]
        l += 1
        r -= 1


def counter(disk):
    total = 0
    for i, v in enumerate(disk):
        if v == ".":
            # break was for pt1
            # break
            # for pt2 we can encounter empty
            continue
        else:
            total += i * int(v)
    print(f"Total: {total}")


def solve():
    data = parse_input()
    disk = unfurl_input(data)
    # print(f"Disk: {disk}")
    swapper(disk)
    counter(disk)
    # print(f"Disk: {disk}")


def solve_p2(cells, datas, frees):
    for data in reversed(datas):
        for free_i in range(len(frees)):
            # data doesn't have a free before it, break loop
            if frees[free_i][2] > data[2]:
                break

            if frees[free_i][1] >= data[1]:
                # set values in cell list
                for i in range(data[1]):
                    cells[frees[free_i][2] + i] = data[0]
                    cells[data[2] + i] = 0

                # update free size and position
                frees[free_i][1] -= data[1]
                frees[free_i][2] += data[1]

                break

    total = sum([max(v - 1, 0) * i for i, v in enumerate(cells)])
    return total


if __name__ == "__main__":
    cells, data, empty = parse_sample_input()
    print(f"Cells: {cells}")
    # print(f"data: {data}")
    # print(f"empty: {empty}")

    print(f"{solve_p2(cells, data, empty)}")
