def binary_search(lst, val):
    # lst is already sorted
    if not lst:
        return -1

    left, right = 0, len(lst)
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


a = [3, 4, 5, 7, 8, 12, 34, 56, 87, 99]

idx = binary_search(a, 37)
print(idx)


