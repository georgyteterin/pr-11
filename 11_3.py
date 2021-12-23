def pod(lis):
    n = max(lis) + 1
    pust = [0] * n
    for i in lis:
        pust[i] += 1
    lis[:] = []
    for j in range(n):
        lis += [j] * pust[j]
    return lis

#4 n