from queue import SimpleQueue

def binary_gen(n):
    q = SimpleQueue()
    q.put("1")
    for _ in range(n):
        b0 = q.get()
        yield b0
        q.put(b0 + "0")
        q.put(b0 + "1")

if __name__ == '__main__':
    for i, n in enumerate(binary_gen(20), 1):
        print(f"{i:2}. 0b{n}")
