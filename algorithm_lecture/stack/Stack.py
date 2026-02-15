class Stack:
    # capacity = 스택 객체의 용량
    def __init__(self, capacity): # 생성자
        self.capacity = capacity
        self.array = [None] * capacity # 비어있는 리스트를 capacity만큼 공간 확보 후 array라는 변수로 명명
        self.top = -1 # 삽입 된 항목이 하나도 없기 때문에 초기 스택 인덱스는 -1로 지정 (인덱스는 0부터 시작하기 때문에 -1 부터면 스택에 항목이 하나도 없다를 의미함)

    # isEmpty (스택이 비어있는지 체크)
    # 스택의 top 인데스의 값이 -1 인지 확인
    def isEmpty(self):
        return self.top == -1

    # isFull (스택에 항목이 꽉 차있는 포화 상태인지 체크)
    # 스택의 top 인덱스의 값이 지정했던 용량과 같은지 판단
    def isFull(self):
        return self.top == self.capacity - 1 # 인덱스는 0 부터 시작이기 때문에 1을 빼줌

    # push (스택이 꽉차있는지 상태를 체크해야함)
    def push(self, value):
        full = self.isFull()

        if full:
            print("Stack Overflow")
            return

        self.top += 1
        self.array[self.top] = value

        # print("push value: ", self.array[self.top])

    # pop (스택에 항목이 비어있는지 체크)
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None

        self.top -= 1 # 감소 시키고
        # print("out value: ", self.array[self.top + 1])
        return self.array[self.top + 1] # 1 감소 시켰으니까 1 더해서 원래 값 리턴

    # Top의 위치를 알면 구할 수 있음 ex) top -> 3 / 개수는 0,1,2,3 총 4개 (* 인덱스는 0부터 시작)
    # 즉 top : top + 1
    def size(self):
        print("size: ", self.top + 1)
        return self.top + 1

    # 스택에 들어있는 데이터들을 화면에 하나씩 출력하는 display
    def display(self):
        for i in range(self.top+1):
            print(self.array[i], " ", end="")
        print()

    # 스택의 상단 요소를 들여다보는 peek
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        return None

# 문제 > 괄호 짝 맞추기
# 입력된 수식에서 왼쪽 여는 괄호와 오른쪽 닫는 괄호의 짝이 맞는지 체크
# input (10+2)*5-5((7-1)/2+9)
# output 괄호짝이 맞으면 True, 아니면 False
def check_brackets():
    inspect_string = input("input: ")

    stack = Stack(len(inspect_string))
    for s in inspect_string:
        if s == "(":
            stack.push(s)
        elif s == ")":
            if stack.isEmpty():
                print("false")
                return
            stack.pop()
        else:
            continue

    if not stack.isEmpty():
        print("false")
        return

    print("true")

    return

if __name__ == "__main__":
    check_brackets()