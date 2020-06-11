

# 递度下降法的第一个公式
def gd1(n,lr=0.01,epoches=2000):
    y = lambda x : x ** 2
    dy_dx = lambda x : 2 * x
    x = 1
    for _ in range(epoches):
        x += lr * (n - y(x)) * dy_dx(x)
    return x

if __name__ == '__main__':
    for n in range(1,10+1):
        print(f"sqrt({n}) = {gd1(n)}")