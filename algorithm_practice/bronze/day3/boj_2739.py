def multiplication_table():
    a = int(input())

    for i in range(1, 10): # 파이썬의 range는 range(start, end)의 경우 end - 1까지다.
        print(a, "*", i, "=" , a * i)

if __name__ == "__main__":
    multiplication_table()