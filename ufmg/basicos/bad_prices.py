

clk = int(input())

for _ in range(clk):

    n = int(input())

    l = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue
    elif n == 2:
        if l[0] > l[1]:
            print(1)
        else:
            print(0)

        continue

    m = l[n - 1]

    ans = 0

    for r in range(n - 1, -1, -1):

        if l[r] > m:
            ans += 1
        elif l[r] < m:
            m = l[r]

    print(ans)