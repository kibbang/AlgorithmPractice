class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity

        # 선형 큐와 다른 부분
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, value):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = value
        else:
            print("Queue Overflow")
            return

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Queue Underflow")
            return None

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self):
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=" ")