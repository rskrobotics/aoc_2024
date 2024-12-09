def parse_input():
    with open("./puzzle_input.txt", "r") as f:
        input = f.read().strip()
    return input


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
            break
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


if __name__ == "__main__":
    # print(f"parse_input{parse_input()}")
    solve()
