

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)



if __name__ == '__main__':
    for i in range(10+1):
        print(fib(i),end=" ")