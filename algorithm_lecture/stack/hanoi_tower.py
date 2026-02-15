"""
n: 옮길 원판의 개수
fr (from): 시작 막대
temp: 임시(보조) 막대
to: 목표 막대

 “fr에 있는 원판 n개를 to로 옮기는데, temp를 보조로 써라” 라는 뜻
 총 이동 횟수 : 2^n - 1
"""
def hanoi(n, fr, temp , to):
    # 1개면 그냥 바로 옮기면 끝
    if n == 1:
        print("원판 1: %s --> %s" % (fr, to))

    # 1) n-1개를 보조로 옮기고
    # 2) 가장 큰 n번 원판을 옮기고
    # 3) 다시 n-1개를 최종으로 옮긴다
    else:
        hanoi(n-1, fr, to , temp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi(n-1, temp, fr , to)

if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')