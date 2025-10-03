def func(n):
    res = []
    i = 2
    while (i<=n):
        if n%i == 0:
            res.append(i)
            n = n//i
        else:
            i += 1
    return res
print(func(int(input())))