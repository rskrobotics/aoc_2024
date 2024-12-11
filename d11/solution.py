from collections import defaultdict


def parse_input():
    stones = defaultdict(lambda: 0)
    with open("./puzzle_input.txt", "r") as f:
        for line in f:
            for e in line.strip().split():
                stones[e] += 1
        for k, v in stones.items():
            print(f"{k}, {v}")
    return stones


def parse_sample_input():
    stones = defaultdict(lambda: 0)
    with open("./sample_input.txt", "r") as f:
        for line in f:
            for e in line.strip().split():
                stones[e] += 1
        for k, v in stones.items():
            print(f"{k}, {v}")
    return stones


def solve(blinks):
    stones = parse_input()
    for i in range(blinks):
        processed = defaultdict(int)
        dbg = []
        for k, v in stones.items():
            dbg.append((k, v))
            if k == "0":
                processed["1"] += v
            elif len(k) % 2 == 0:
                mid = len(k) // 2
                rpart = k[mid:].lstrip("0")
                processed[rpart if rpart else "0"] += v
                processed[k[:mid]] += v
            else:
                processed[str(int(k) * 2024)] += v
        stones = processed
        print(f"DBG: {dbg}")

    total = sum(processed.values())
    print(f"Total: {total}")


if __name__ == "__main__":
    # data = parse_input()
    blinks = 75
    # data = parse_sample_input()
    # print(f"Data: {data}")
    solve(blinks)
