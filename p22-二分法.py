

def sqrt(n,eps = 1e-4):
    y = lambda x:x**2 -n
    xa = 0
    xb = n + 1
    xm = (xa + xb)/2
    while abs(y(xm)) - eps > 0 :
        if y(xm) > 0:
            xb = xm
        else:
            xa = xm
        xm = (xa + xb) / 2

    return xm



if __name__ == '__main__':
    for i in range(1,10+1):
        print(f"sqrt({i}) = {sqrt(i)}")