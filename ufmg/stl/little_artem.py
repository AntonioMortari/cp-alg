

n = int(input())

for _ in range(n):

    n,m = map(int, input().split())

    ans = []

    for i in range(n):
        ans.append([])
        if i == 0:

            for j in range(m):

                if j == 0:
                    ans[i].append('W')
                else:
                    ans[i].append('B')

        else:
            for j in range(m):
                    ans[i].append('B')

    for l in ans:
        print("".join(l))