def mergesort(target: list):
    if len(target) <= 1:
        return target

    mid = len(target) // 2
    left = target[:mid]
    right = target[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left,right):
    merged = []

    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1

        else:
            merged.append(right[r])
            r += 1

    if l < len(left):
        merged.extend(left[l:])
    if r < len(right):
        merged.extend(right[r:])

    return merged



