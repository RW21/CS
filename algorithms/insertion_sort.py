def insertion_sort(target: list) -> list:
    i = 1
    while i < len(target):
        j = i
        while j > 0 and target[j-1] > target[j]:
            target[j], target[j-1] = target[j-1], target[j]
            j -= 1
        i += 1

# example
a = [1,3,5,2,5]
insertion_sort(a)
print(a)
