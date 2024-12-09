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


def find_empty_length(data):
    seq = 0
    for e in data:
        if e == ".":
            seq += 1
        else:
            break
    return seq


def swapper_2(disk):
    l, r = 0, len(disk) - 1
    while l < r:
        while l < len(disk) and disk[l] != ".":
            l += 1
        if l >= len(disk):
            break
        space = find_empty_length(disk[l:])
        while r >= 0 and disk[r] == ".":
            r -= 1
        if r < 0:
            break
        seq = 1
        while r > 0 and disk[r - 1] == disk[r]:
            seq += 1
            r -= 1
        if seq <= space:
            print(f"SEQ: {seq} space: {space}")
            print(f"SWAPPING: {l} {r}")

            disk[l : l + seq], disk[r : r + seq] = disk[r : r + seq], disk[l : l + seq]
            l += space

            if l > r:
                l, r = 0, len(disk) - 1
        else:
            print(f"Failed swap: {l}/{r}")
            r -= 1
        print(f"DISK: {disk}")
    print(f"DONE! {disk}")


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
    swapper_2(disk)
    counter(disk)
    # print(f"Disk: {disk}")


if __name__ == "__main__":
    # print(f"parse_input{parse_input()}")
    disk = "00...111...2...333.44.5555.6666.777.888899"
    print(f"LEN DISK : {len(disk)}")
    disk = list(disk)
    print(f"DISK: {disk}")
    print(swapper_2(disk))
    # solve()
