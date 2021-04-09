
def quick_sort(lst):
    if not lst and len(lst) < 2:
        return lst

    pivot = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        if lst[i] <= pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


a = [9, 6, 7, 4, 8, 3, 0, 12, -7]

a_sorted = quick_sort(a)
print(a_sorted)
