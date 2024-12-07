def parse_file():
    rules = []
    updates = []
    parsing_rules = True

    with open("./puzzle_input.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                parsing_rules = False
                continue

            if parsing_rules:
                a, b = map(int, line.split("|"))
                rules.append((a, b))
            else:
                updates.append(tuple(map(int, line.split(","))))

    return rules, updates


def solve_pt1():
    rules, updates = parse_file()
    sum_of_middles = 0
    incorrect_indexes = []

    for idx, update in enumerate(updates):
        numbers = {}
        should_add = True
        for i, f in enumerate(update):
            numbers[f] = i
        for r1, r2 in rules:
            if r1 in numbers and r2 in numbers:
                if numbers[r1] > numbers[r2]:
                    should_add = False
                    incorrect_indexes.append(idx)
                    break
        if should_add:
            sum_of_middles += update[len(update) // 2]
    part2(rules, updates, incorrect_indexes)


def part2(rules, updates, incorrect_indexes):
    middle_sum = 0
    for inc in incorrect_indexes:
        update = list(updates[inc])
        i = 0
        while i != len(update):
            i = len(update)
            for r1, r2 in rules:
                if r1 not in update or r2 not in update:
                    continue
                l, r = update.index(r1), update.index(r2)
                if l > r:
                    i -= 1
                    update.pop(l)
                    update.insert(r, r1)

        middle_sum += update[len(update) // 2]


if __name__ == "__main__":
    # rules, updates = parse_file()
    # print("Rules:")
    # for values in rules:
    #    print(f"VALUES: {values}")

    # print("\nUpdates:")
    # for update in updates:
    #    print(update)
    solve_pt1()
