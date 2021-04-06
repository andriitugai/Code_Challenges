
def merge_sort(lst):
    def merge(a, b):
        ia, ib = 0, 0

        result = []
        while ia < len(a) and ib < len(b):
            if a[ia] <= b[ib]:
                result.append(a[ia])
                ia += 1
            else:
                result.append(b[ib])
                ib += 1

        if ia < len(a):
            result += a[ia:]
        elif ib < len(b):
            result += b[ib:]

        return result

    if not lst or len(lst) < 2:
        return lst

    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


a = [9, 6, 7, 4, 5, 8, 3, 0, 12, -7]

a_sorted = merge_sort(a)
print(a_sorted)

