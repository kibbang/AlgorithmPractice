def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result = result * k

    return result

def factorial_recur(n):
    if n == 1:
        return 1

    return n * factorial_recur(n - 1) # 호출 할 수록 크기가 작아져야함

if __name__ == '__main__':
    print(factorial_iter(5))
    print("--------------factorial_recur-----------------")
    print(factorial_recur(5))