from math import sqrt

n = int(input())

for _ in range(n):

    num = int(input())

    prime = True

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            prime = False    

    if prime:
        print("Prime")
    else:
        print("Not Prime")