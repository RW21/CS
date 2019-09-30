# O(log(n))

def binary_search(l: list, target: int) -> int:
    first, last = 0, len(l) - 1
    while first <= last:
        middle = (first + last) // 2
        if l[middle] == target:
            return middle
        else:
            if target < l[middle]:
                last = middle - 1
            else:
                first = middle + 1
