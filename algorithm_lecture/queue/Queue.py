class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.rear = -1
        self.front = -1

    # 큐가 비어있는지 확인
    def is_empty(self):
        return self.front == self.rear

    # 큐가 다 찼는지 확인
    def is_full(self):
        return self.rear == self.capacity - 1 # 인덱스는 0부터 시작이니까

    # 항목 삽입
    def enqueue(self, value):
        if not self.is_full():
            self.rear += 1 # 맨 뒤 인덱스에 넣어야하니까 증가시키고
            self.array[self.rear] = value # 그 인덱스에 값을 넣는다.
        else:
            print("Overflow")

    # 항목 제거
    def dequeue(self):
        if not self.is_empty(): # 큐가 비어있는지 체크
            self.front += 1 # front를 1 증가시켜서 큐의 맨 앞 항목을 가르키게 한다.
            return self.array[self.front]
        else:
            print("Underflow")
            return None

    # 큐의 갯수 확인
    def size(self):
        return self.rear - self.front # rear와 front 사이에 남아있는 항목들이 큐에 남아있는 데이터의 개수

    # 큐의 모든 항목 출력
    def display(self):
        for i in range(self.front + 1, self.rear +1):
            print(self.array[i], end=" ")

def test():
    q = Queue(10)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)
    q.enqueue(110)

    q.dequeue()
    q.dequeue()
    q.display()

    print()
    print(q.size())
    print(q.front, q.rear)
    print(q.is_full())


    q.enqueue(110)

if __name__ == "__main__":
    test()