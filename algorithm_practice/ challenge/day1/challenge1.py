'''
Big-O = n
최악의 경우 리스트의 개수만큼 연산이 수행될 수 있다.
'''
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

'''
Big-O = n
최악의 경우 리스트의 개수만큼 연산이 수행될 수 있다.
'''

'''
작성 내용: n-1/2, 최고차항 n으로 계산됨
정답: $O(\log n)$이유: 이진 탐색은 한 번 확인할 때마다 탐색 범위가 **절반(1/2)**씩 줄어듭니다.
데이터가 $16 \to 8 \to 4 \to 2 \to 1$ 순으로 줄어드는 연산은 로그 함수로 표현됩니다.
'''
def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

'''
0 1 2 3 4 5

n -1 / 2 가 나오는데 이는 최고차항 n으로 계산됨 
'''

'''
작성 내용: n-1/2, 최고차항 n으로 계산됨
정답: $O(\log n)$이유: 이진 탐색은 한 번 확인할 때마다 탐색 범위가 **절반(1/2)**씩 줄어듭니다.
데이터가 $16 \to 8 \to 4 \to 2 \to 1$ 순으로 줄어드는 연산은 로그 함수로 표현됩니다.
'''
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

'''
n개의 원소를 가진 데이터 컬렉션에서 특정 값 target이 존재하는지 확인하는 in 연산을 수행하려고 합니다. list와 set 자료구조를 사용할 때의 시간 복잡도를 빅오(Big-O) 표기법으로 각각 서술하고, 왜 성능 차이가 발생하는지 각 자료구조의 내부 동작 원리와 연관 지어 설명하세요.

target in my_list (단, my_list는 n개의 원소를 가진 리스트)
target in my_set (단, my_set은 n개의 원소를 가진 세트

list -> n $O(n)$처음부터 하나씩 대조하는 순차 탐색 방식
set -> n? $O(1)$해시 함수를 통해 값의 위치를 즉시 계산하는 방식

'''

'''
n개의 원소를 가진 데이터 컬렉션에서 맨 앞의 원소를 제거하는 연산을 수행하려고 합니다. 파이썬의 list에서 pop(0)를 사용하는 것과 collections.deque에서 popleft()를 사용하는 것의 시간 복잡도를 빅오(Big-O) 표기법으로 각각 서술하고, 왜 성능 차이가 발생하는지 각 자료구조의 내부 동작 원리와 연관 지어 설명하세요.

my_list.pop(0) (단, my_list는 n개의 원소를 가진 리스트)
my_deque.popleft() (단, my_deque는 n개의 원소를 가진 deque)

list -> n $O(n) 0번을 빼낸 후, 나머지 모든 원소를 앞으로 한 칸씩 이동시켜야 함
deque -> 1 $O(1)$ 내부가 연결 리스트 구조라 포인터 위치만 변경하면 끝남

'''