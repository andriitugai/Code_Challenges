# sorted
def two_sum_sorted(lsts, target):
    result = []
    if not lsts or len(lsts) < 2:
        return result

    left, right = 0, len(lsts) - 1
    while left < right:
        sm = lsts[left] + lsts[right]
        if sm == target:
            result.append((lsts[left], lsts[right]))
            left += 1
            right -= 1
        elif sm > target:
            right -= 1
        else:
            left += 1

    return result


# a = [1, 2, 3, 4, 5, 6, 7, 10]
# print(two_sum_sorted(a, 8))


def two_sum_unsorted(lst, target):
    result = []
    if not lst or len(lst) < 2:
        return result

    ht = {}
    for num in lst:
        addition = target - num
        if addition not in ht:
            ht[num] = addition
        else:
            result.append((addition, ht[addition]))

    return result


# a = [1, 9, 5, 8, 2, 3, 4, 1, 5, 0, 6, 7, 10]
# print(two_sum_unsorted(a, 15))


def three_sum(lst, target):
    result = []
    if not lst or len(lst) < 3:
        return result

    lsts = sorted(lst)
    idx = 0
    while idx < len(lsts) - 2:
        t2 = target - lsts[idx]
        for pair in two_sum_sorted(lsts[idx+1:], t2):
            result.append((lsts[idx], pair[0], pair[1]))

        idx += 1

    return result


a = [1, 9, 5, 8, 2, 3, 4, 1, 5, 0, 6, 7, 10]
print(three_sum(a, 10))

