def merge_sort_inplace(target):
    unit = 1

    while unit <= len(target):
        h = 0
        for h in range(0, len(target), unit * 2):
            l = h
            r = min(len(target), h + 2 * unit)
            mid = h + unit
            p = l
            q = mid

            while p < mid and q < r:
                if target[p] < target[q]:
                    p += 1
                else:
                    tmp = target[q]
                    target[p + 1: q + 1] = target[p:q]
                    target[p] = tmp
                    p += 1
                    mid += 1
                    q += 1

        unit *= 2

    return target
