import heapq


def get_k_max_elements(lst, k):
    h = []
    for item in lst:
        heapq.heappush(h, item)
        if len(h) > k:
            heapq.heappop(h)

    return h


if __name__ == '__main__':
    a = [2, 67, 34, 92, 11, 1, -5, 87]
    print(get_k_max_elements(a, 3))
