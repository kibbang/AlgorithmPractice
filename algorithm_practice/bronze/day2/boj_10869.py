from math import floor


def four_basic_operations():
    a,b = map(int, input().split())

    print(a + b)
    print(a - b)
    print(a * b)
    print(floor(a / b))
    print(a % b)

if __name__ == "__main__":
    four_basic_operations()
