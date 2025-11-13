height = list(map(int, input().split()))
result = []

for i in range(len(height)):
    base = -1
    for j in range(i-1, -1, -1):
        if height[j] > height[i]:
            base = j
            break
    result.append(base)

print(' '.join(map(str, result)))