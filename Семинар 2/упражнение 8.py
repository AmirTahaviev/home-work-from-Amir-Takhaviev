a = list(map(int, input().split()))
def med(s):
    for i in range(len(s)):
        i1 = 0
        i2 = 0
        for j in range(len(s)):
            if s[i] > s[j]:
                i1 += 1
            elif s[i] < s[j]:
                i2 += 1
        if i1 - 1  == i2:
            return a[i]
        else:
            continue
    if i1 == i2:
        return s[i]
    return None
print(med(a))