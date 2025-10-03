import numpy as np
def f(N,M):
    m = np.zeros((N, M))
    for i in range(N):
        m[i,0:M]=input().split()
    coef = m[0:N,0:M-1]
    end = m[0:N,M-1:M]

    print(np.linalg.solve(coef,end))
N,M=map(int,input().split())
f(N,M)

