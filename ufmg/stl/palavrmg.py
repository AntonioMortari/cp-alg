

n = int(input())

w = []

def is_sorted(p: str):
    n = len(p)
    if n == 1:
        return True

    l = 0

    for r in range(1, n):

        if (ord(p[r]) - ord('a')) <= (ord(p[l]) - ord('a')):
            return False

        l += 1

    return True

        

for _ in range(n):
    p = input()

    pl = p.lower()

    w.append((p, is_sorted(pl)))

for p,o in w:

    if o:
        print(f"{p}: O")
    else:
        print(f"{p}: N")
