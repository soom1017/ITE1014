def comb(n, r):
    if r == 0:
        return 1
    elif r == 1:
        return n
    elif r == n:
        return 1
    else:
        return comb(n-1,r-1) + comb(n-1,r)

n, r = input().split()
print(comb(int(n),int(r)))
