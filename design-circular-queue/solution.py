class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.store = [None] * k
        self.head = 0
        self.tail = -1
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.size
        self.store[self.tail] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.length -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.store[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.store[self.tail]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
