

n = int(input())

for i in range(n):

    s1, s2 = input().split()

    if s1 in s2+s2:
        print('S')
    elif s1 == s2[::-1]:
        print('S')
    elif s1 in s2[::-1]+s2[::-1]:
        print('S')
    else:
        print('N')