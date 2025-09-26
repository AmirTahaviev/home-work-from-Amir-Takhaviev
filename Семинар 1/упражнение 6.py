f = open('ex2.txt', 'r+')
a = f.readlines()
n0 =  list(map(int, a[0].split()))
sign = a[1].strip()

n = int(a[2])

n1 = [0, 0, 0]

for j in range(0, 3):
    l = list(map(int, str(n0[j])[::1]))
    for i in range(0, len(l)):
        n1[j] = n1[j] + l[i]*n**(len(l)-1-i)

def t(k):
    r = []
    while k != 0:
        r.append(k % n)
        k = k // n
    return ''.join(map(str, r[::-1]))

if sign == '+':
    f.write(t(n1[0]+n1[1]+n1[2]))
    print(t(n1[0]+n1[1]+n1[2]))
elif sign == '*':
    f.write((t(n1[0]*n1[1]*n1[2])))
    print((t(n1[0]*n1[1]*n1[2])))
elif sign == '-':
    f.write((t(n1[0] - n1[1] - n1[2])))
    print((t(n1[0] - n1[1] - n1[2])))

f.close()