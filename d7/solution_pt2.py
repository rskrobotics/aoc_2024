from math import prod


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


class CalibrationTree:
    def __init__(self, pair):
        self.pair = pair
        self.sum = None
        self.prod = None
        self.concat = None

    def add_children(self, number):
        self.sum = CalibrationTree([sum(self.pair), number])
        self.prod = CalibrationTree([prod(self.pair), number])
        self.concat = CalibrationTree(
            [int(str(self.pair[0]) + str(self.pair[1])), number]
        )


def add_nodes(node, number):
    if node.sum is None:
        node.add_children(number)
        return
    add_nodes(node.sum, number)
    add_nodes(node.prod, number)
    add_nodes(node.concat, number)


def get_totals(node, total_list):
    if node.sum is None:
        total_list.append(sum(node.pair))
        total_list.append(prod(node.pair))
        total_list.append(int(str(node.pair[0]) + str(node.pair[1])))
        return total_list
    total_list = get_totals(node.sum, total_list)
    total_list = get_totals(node.prod, total_list)
    total_list = get_totals(node.concat, total_list)
    return total_list


if __name__ == "__main__":
    passing_tvals = []
    data = parse_file()

    for tvalue, numbers in data:
        root = CalibrationTree(numbers[:2])
        numbers = numbers[2:]
        for num in numbers:
            add_nodes(root, num)
        total_list = get_totals(root, [])
        if tvalue in total_list:
            passing_tvals.append(tvalue)

    print(sum(passing_tvals))
