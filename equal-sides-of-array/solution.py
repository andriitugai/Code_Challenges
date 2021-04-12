def find_even_index(arr):
    total = sum(arr)
    running = 0
    for i, item in enumerate(arr):
        if running * 2 + item == total:
            return i
        running += item

    return -1


if __name__ == '__main__':
    arr = [-9, -12, 6, 60, 17, -4, 5, 10, -4, -9, 6, 11, 17, 13, -12, 17, 18, -9]
    e_idx = find_even_index(arr)
    print(f'Even-index: {e_idx}, {sum(arr[:e_idx])} <===> {sum(arr[e_idx+1:])}')
