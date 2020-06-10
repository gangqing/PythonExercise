
def fac1(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def fac2(n):
    result = [1]
    for i in range(2,n+1):
        mul(result,i)
    return toString(result)

def mul(result,a):
    add  =0
    for position in range(len(result)):
        aa = result[position] * a + add
        result[position] = aa % 10
        add = aa // 10

    while add > 0:
        result.append(add % 10)
        add //= 10

def toString(result):
    return "".join([str(e) for e in reversed(result)])


if __name__ == '__main__':
    for n in range(1,100+1):
        print(f"{n} != {fac2(n)}")