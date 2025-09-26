import math
N = list(map(int, input().split()))
x = 1

for i in range(0, len(N)):
    x = x * N[i]
    i+=1
print(x ** (1/len(N)))

