def quick_sort(target: list) -> list:
    less = []
    equal = []
    greater = []

    if len(target) > 0:
        pivot = len(target) // 2
        for i in target:
            if i == target[pivot]:
                equal.append(i)
            if i < target[pivot]:
                less.append(i)
            if i > target[pivot]:
                greater.append(i)
        
        return quick_sort(less) + equal + quick_sort(greater)

    return target  