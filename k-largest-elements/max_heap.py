import heapq


def get_k_min_elements(lst, k):
    class MaxHeap:
        def __init__(self):
            self.data = []

        def push(self, val):
            heapq.heappush(self.data, -val)

        def pop(self):
            return -heapq.heappop(self.data)

        def size(self):
            return len(self.data)

        def to_list(self):
            return list(map(lambda x: -x, self.data))

    max_heap = MaxHeap()
    for elem in lst:
        max_heap.push(elem)
        if max_heap.size() > k:
            max_heap.pop()

    return max_heap.to_list()


if __name__ == '__main__':
    a = [2, 67, 34, 92, 11, 1, -5, 87]
    print(get_k_min_elements(a, 3))
