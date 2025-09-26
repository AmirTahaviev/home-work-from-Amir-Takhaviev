N, s = input().split()
N = int(N)
n_len = len(s)//N
res = ''
for i in range(0, len(s), n_len):
    res += s[i:i+n_len][::-1]
print(res)