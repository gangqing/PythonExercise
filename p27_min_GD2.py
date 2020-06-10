

import p26_Exp as ep


def argMin(exp,x,lr=0.01,epoches=2000):
    dy_dx = exp.deriv(x)
    x = 1
    for _ in range(epoches):
        x += -lr * dy_dx.eval(x=x)

    return x


if __name__ == '__main__':
    x = ep.Variable("x")
    y = ep.Variable("y")

    while True:
        exp = input("> please input exp : ")
        if len(exp) == 0:
            break
        exp = eval(exp)
        print(exp)
        min_x = argMin(exp,x)
        print(f"x = {min_x},min_value = {exp.eval(x=min_x)}")