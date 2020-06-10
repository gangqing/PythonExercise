# 五猴分桃

def getPeaches(monkeys):
    # 初始化桃子数
    peaches = monkeys + 1
    # 判断桃子是否够分
    while not dividable(peaches,monkeys):
        # 递增
        peaches += monkeys
    return peaches

def dividable(peaches,monkeys):
    for _ in range(monkeys):
        peaches -= 1
        if peaches % monkeys != 0:
            return False
        peaches = peaches // monkeys * (monkeys - 1)
    return True

if __name__ == '__main__':
    print(getPeaches(5))