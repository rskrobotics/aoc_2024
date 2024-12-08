def parse_file():
    data = []
    with open("./puzzle_input.txt", "r") as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                tvalue, values = line.split(":")
                tvalue = int(tvalue.strip())
                values_list = [int(num) for num in values.strip().split()]
                data.append([tvalue, values_list])
    return data


def calculate(nums):
    if len(nums) == 1:
        return nums

    return calculate([nums[0] + nums[1]] + nums[2:]) + calculate(
        [nums[0] * nums[1]] + nums[2:]
    )


def solve_pt1():
    total = 0
    d = parse_file()

    for l in d:
        posibilities = calculate(l[1])

        if l[0] in posibilities:
            total += l[0]

    print(f"Total: {total}")


if __name__ == "__main__":
    # input = parse_file()
    # pprint(input)
    solve_pt1()
