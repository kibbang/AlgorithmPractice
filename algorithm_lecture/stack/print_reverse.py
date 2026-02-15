"""
문자 거꾸로 찍기
"""
def print_reverse(msg, length):
    # expect -> 조구료자
    if length == 0:
        return
    print_reverse(msg[1:], length - 1)
    print(msg[0], end="")

if __name__ == '__main__':
    input_msg = input()
    print_reverse(input_msg, len(input_msg))

"""
자료구조 -> 4

print_reverse(자료구조, 4)
print_reverse(료구조, 3)
print_reverse(구조, 2)
print_reverse(조, 1)
print_reverse("", 0)리턴

리턴 된 후 더이상 print_reverse 호출이 없으니까

print(msg[0]) 이게 찍혀서 가장 첫 글자가 순서대로 찍힘

조구료자
"""


