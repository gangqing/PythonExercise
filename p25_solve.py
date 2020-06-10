import math

def slove_min(dy_dx,lr = 0.01,epoches = 2000):
    x = 1
    for i in range(epoches):
        dx = -lr * dy_dx(x)
        x += dx
    return x

def slove(y,dy_dx,value,lr=0.01,epoches=2000):
    loss = lambda x : (y(x) - value)**2
    loss_dx = lambda x : 2 * (y(x) - value) * dy_dx(x)
    x = 1
    dx = lambda x : -lr * loss_dx(x)
    for _ in range(epoches):
        x += dx(x)
    return x


if __name__ == '__main__':
    # 求函数sin(x)最小值时的解
    y = lambda x : math.sin(x)
    dy_dx = lambda x : math.cos(x)
    x = slove_min(dy_dx)
    print(f"sin({x}) = {y(x)}")

    # 求函数sin(x) = n时的解
    n = 0.5
    y = lambda x : math.sin(x)
    dy_dx = lambda x : math.cos(x)
    x = slove(y,dy_dx,n)
    print(f"sin({x}) = {y(x)}")

    # 求函数x**3 = n时的解
    n = 2
    y = lambda x : x**3
    dy_dx = lambda x : 2 * x**2
    x = slove(y,dy_dx,n)
    print(f"{x}**3 = {y(x)}")

    # 求e**(sin(x))的最大值
    y = lambda x : -math.e**(math.sin(x))
    dy_dx = lambda x : math.cos(x) * y(x)
    x = slove_min(dy_dx)
    print(f"e**(sin(x))的最大值是{-y(x)}")