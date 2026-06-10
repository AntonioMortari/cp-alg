from math import sqrt

n = int(input())

prime = True

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        prime = False

if prime:
    print("sim")
else:
    print("nao")