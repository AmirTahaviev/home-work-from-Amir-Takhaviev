from itertools import count
with open('9 problem.txt', 'r') as f:
    t = "".join(f.readlines())

l = ['.', '!', '?', '...']
k = 0
for i in range(len(t)-1):
    if t[i+1] in l and t[i] not in l:
        k = k +1
print(k)