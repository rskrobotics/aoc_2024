class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def parse_input():
    dummy = Node(0)
    curr = dummy
    with open("./puzzle_input.txt", "r") as f:
        for line in f:
            for e in line.strip().split():
                new = Node(e)
                curr.next = new
                curr = new

    dbg = dummy.next
    while dbg:
        print(f"dbg.val: {dbg.val}")
        dbg = dbg.next
    return dummy


def parse_sample_input():
    dummy = Node(0)
    curr = dummy
    with open("./sample_input.txt", "r") as f:
        for line in f:
            for e in line.strip().split():
                new = Node(e)
                curr.next = new
                curr = new

    dbg = dummy.next
    while dbg:
        print(f"dbg.val: {dbg.val}")
        dbg = dbg.next
    return dummy


def solve(blinks):
    dummy = parse_input()
    for i in range(blinks):
        print("Blinking!")
        head = dummy.next
        # dbg = []
        while head:
            # dbg.append(head.val)
            if int(head.val) == 0:
                head.val = "1"
                head = head.next
            elif len(head.val) % 2 == 0:
                tmp = head.next
                new = Node(str(int(head.val[len(head.val) // 2 :])))
                head.val = head.val[: len(head.val) // 2]
                head.next = new
                new.next = tmp
                head = head.next.next
            else:
                head.val = str(int(head.val) * 2024)
                head = head.next
        # print(f"DBG: {dbg}")

    total = 0
    head = dummy.next
    while head:
        total += 1
        head = head.next

    print(f"Total: {total}")


if __name__ == "__main__":
    # data = parse_input()
    blinks = 75
    # data = parse_sample_input()
    # print(f"Data: {data}")
    solve(blinks)
