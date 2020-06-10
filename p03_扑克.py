
def getList(n):
    result = [n]
    for poke in range(n-1,0,-1):
        a = poke % len(result)
        for _ in range(a):
            flip(result)
        result.insert(0,poke)
    return result

def flip(result):
    poke = result[-1]
    del result[-1]
    result.insert(0,poke)

if __name__ == '__main__':
    print(getList(20))