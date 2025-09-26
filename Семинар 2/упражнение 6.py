n = list(map(int, input().split()))

for i in range(len(n)):
    c = 0
    for j in range(len(n)):
        if n[i] == n[j]:
            c += 1
    if c == 1:
        print(n[i])