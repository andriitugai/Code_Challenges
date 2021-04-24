from queue import SimpleQueue


def binary_gen(n, width):
    q = SimpleQueue()
    yield f'0b{0:0>width}'
    q.put("1")
    for _ in range(n-1):
        b0 = q.get()
        yield f'0b{b0:0>{width}}'
        q.put(b0 + "0")
        q.put(b0 + "1")

if __name__ == '__main__':
    for i, b in enumerate(binary_gen(20,6), 0):
        print(f"{i:2}. b")
