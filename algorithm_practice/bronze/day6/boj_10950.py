def add_num():
    count = int(input())

    for i in range(count):
        a,b = map(int, input().split())

        print(a + b)

if __name__ == "__main__":
    add_num()
