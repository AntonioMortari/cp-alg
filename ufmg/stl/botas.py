

n = int(input())

ans = 0
l = []

for i in range(n):

    num, t = input().split()

    if num+t not in l:
        if t == 'E':
            t = 'D'
        else:
            t = 'E'
        l.append(num+t)
    else:
        ans += 1
        l.remove(num+t)

print(ans)
