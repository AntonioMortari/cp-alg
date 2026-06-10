
clk = 1

while True:
    n = int(input())

    if n == 0:
        break

    l = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        if i + 1 == l[i]:
            ans = i + 1

    print(f"Teste {clk}")
    print(ans)
    clk += 1