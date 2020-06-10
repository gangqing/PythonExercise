
# 递度下降法的第二个公式

def sqrt(n,lr=0.001,epoches=2000):
    y = lambda x : x**2
    dy_dx = lambda x : 2 * x
    # l2损失函数
    loss = lambda x : (y(x) - n)**2
    loss_dx = lambda  x : 2 * (y(x) - n) * dy_dx(x)
    # 求损失函数的最小值
    dx = lambda x : -lr * loss_dx(x)
    x = 1
    for _ in range(epoches):
        x += dx(x)
    return x


if __name__ == '__main__':
    # 求n的开方
    for n in range(1,10+1):
        print(f"sqrt({n}) = {sqrt(n)}")