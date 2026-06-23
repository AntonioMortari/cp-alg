

clk = int(input())

for _ in range(clk):

    c,n = map(int, input().split())

    curr = {'JD': 1}

    ans = 0

    for i in range(c):
        ci, vi = input().split()

        curr[ci] = float(vi)

    for i in range(n):

        v,c = input().split()

        v = float(v)

        ans += v * curr[c]

    print(f"{ans:.6f}")