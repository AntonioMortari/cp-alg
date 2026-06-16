

n = int(input())

for _ in range(n):

    a,b,x,y = map(int, input().split())

    l = x * b
    r = (a - x - 1) * b
    u = y * a
    d = (b - y - 1) * a

    print(max(l,r,u,d))
    