
import random
def func(n):
    list = [False] * n
    light = False
    while False in list:
        countor = 0
        a = random.randint(0,n-1)
        print(f"{getName(a,countor)},{getWake(list[a])},{getLight(light)}")
        prisoner = list[a]
        if a == countor and light:
            list[a] = True
            light = False
            print("操作：关灯")
        elif (not prisoner) and (not light):
            light = True
            list[a] = True
            print("操作：开灯")

def getName(a,countor):
     return "计数人" if a == countor else f"{a}号囚犯"

def getWake(prisoner):
    return "守过夜" if prisoner else "没守过夜"

def getLight(bool):
    return "灯是开着的" if bool else "灯是关着的"


if __name__ == '__main__':
    func(4)