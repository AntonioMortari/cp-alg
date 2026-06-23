

n = int(input())

for i in range(n):

    q = list(input())

    ans = 0
    x,y = 0,0
    
    v = set()
    v.add(((x,y), (x,y)))

    for p in q:

        prevx, prevy = x,y

        if p == 'N':
            x -= 1
        elif p == 'S':
            x += 1
        elif p == 'E':
            y += 1
        elif p == 'W':
            y -= 1

        if ((prevx, prevy), (x,y)) in v or ((x, y), (prevx,prevy)) in v:
            ans += 1
        else:
            ans += 5

        v.add(((prevx, prevy), (x,y)))

    print(ans)
