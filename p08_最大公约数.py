


def gcd(a,b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a > b :
        a,b = b,a
    while a > 0:
        b,a = a,b%a
    return b

if __name__ == '__main__':
    for i in range(1,10 + 1):
        for j in range(1,10 + 1):
            print(f"gcd({i},{j}) = {gcd(i,j)}")
        pass
    pass

