

n = int(input())

for i in range(n):

    a,b = map(int, input().split())

    if a == b:
        print(0)
        continue

    diff = abs(a - b)

    if a > b:
        if diff % 2 == 0 and b % 2 == 0:
            print(1)
        elif diff % 2 == 0 and b % 2 > 0:
            print(1)
        else:
            print(2)
    else:
        if diff % 2 == 0 and b % 2 == 0:
            print(2)
        elif diff % 2 == 0 and b % 2 > 0:
            print(2)
        else:
            print(1)
