
h = set()

while True:
    try:
        h.add(input().strip()) 
    except EOFError:
        break

print(len(h))