

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

ans = []

find = False

for i in range(n):

    for j in range(m):

        s = a[i] + b[j] 
        if s not in a and s not in b:
            ans.append(a[i])
            ans.append(b[j])
            find = True
            break

    if find:
        break

print(*ans)
            