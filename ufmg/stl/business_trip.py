

k = int(input())

l = list(map(int, input().split()))

acc = 0

ans = 0

if k == 0:
    print(0)
else:

    while len(l) > 0:

        m = max(l)

        acc += m

        l.remove(m)

        ans += 1

        if acc >= k:
            break
        
    if acc < k:
        print(-1)
    else:
        print(ans)