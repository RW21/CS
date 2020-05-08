from data_structures import queue, stack

s1 = stack.Stack()
s2 = stack.Stack()
s3 = stack.Stack()

# not flexible
def list_to_three_stacks(l: list, s1, s2, s3):
    ranges = [0, len(l) // 3, len(l) // 3 + 1, len(l) // 3 * 2, len(l) // 3 * 2 + 1, len(l) - 1]
    print(ranges)

    for i in range(ranges[0], ranges[1] + 1):
        s1.push(l[i])

    for i in range(ranges[2], ranges[3] + 1):
        s2.push(l[i])

    for i in range(ranges[4], ranges[5] + 1):
        s3.push(l[i])



