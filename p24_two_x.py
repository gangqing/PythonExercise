
# 两个变量的最小值求解

def solve(lr=0.01,epoches=2000):
    y = lambda x1,x2 : (x1 - 3)**2 + (x2 + 4)**2
    dy_dx1 = lambda x1,x2 : 2 * (x1 - 3)
    dy_dx2 = lambda x1,x2 : 2 * (x2 + 4)
    dx1 = lambda x1,x2 : -lr * dy_dx1(x1,x2)
    dx2 = lambda x1,x2 : -lr * dy_dx2(x1,x2)

    x1 = 1
    x2 = 1
    for _ in range(epoches):
        x1 += dx1(x1,x2)
        x2 += dx2(x1,x2)

    return x1,x2




if __name__ == '__main__':
    print(f"x1,x2={solve()}")