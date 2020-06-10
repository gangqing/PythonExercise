
# 牛顿法
def sqrt(n,epoches = 5):
    x = 1
    for _ in range(epoches):
        x = (n + x**2) / (2 * x)
    return x

if __name__ == '__main__':
    for n in range(1,10+1):
        print(f"sqrt({n}) = {sqrt(n)}")