from pprint import pprint

from algorithm_lecture.stack.Stack import Stack

def main():
    size = 10
    s1 = create_stack(size)

    stack_push(s1)

    stack_pop(s1)

    stack_size(s1)

    stack_display(s1)

    print()

    pprint(vars(s1))

def stack_push(s1: Stack):
    s1.push(10)
    s1.push(20)
    s1.push(30)

def stack_pop(s1: Stack):
    s1.pop()
    s1.pop()  # top 0이 나오는데 이는 0번째 인덱스만 유효하다는 뜻
    s1.pop()
    s1.pop()
    s1.pop()


def stack_size(s1: Stack):
    s1.size()

def stack_display(s1: Stack):
    s1.display()

def create_stack(size) -> Stack:
    return Stack(size)

if __name__ == '__main__':
    main()