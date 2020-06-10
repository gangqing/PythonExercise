import math

NAMES = "赵权孙武张邓林李王彭蓝黄梁方刘"

def getPages(names):
    n = int(math.log(len(names),2)) + 1
    pages = ["" for _ in range(n)]
    for i in range(len(names)):
        position = i + 1 # 姓名位置
        for j in range(n): # 页位置
            if position % (2) == 1:
                pages[j] += names[i] + ","
            position = position // 2
    return pages

def getName(names,result):
    position = 0
    for i in range(len(result)):
        value = result[i]
        position += 2**i * value
    return names[position - 1]

if __name__ == '__main__':
    pages = getPages(NAMES)
    result = []
    for page in pages:
        print(page)
        answer = input("Is your name in this page?(y/n)")
        if answer.lower() == "y":
            result.append(1)
        else:
            result.append(0)
    print(f"your name is {getName(NAMES,result)}")



