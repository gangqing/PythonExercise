
import math

class Exp:
    # **value : x=1,y=2
    # return : 计算结束
    def eval(self,**value):
        pass

    def simplify(self): # return : 表达式
        return self

    def deriv(self,x): # return : 导数结果
        pass

    def __add__(self, other): # self + other
        return Add(self,toExp(other)).simplify()

    def __radd__(self, other):
        return Add(toExp(other),self).simplify()

    def __sub__(self, other): # self - other
        return Sub(self, toExp(other)).simplify()

    def __rsub__(self, other):
        return Sub(toExp(other), self).simplify()

    def __mul__(self, other): # self * other
        return Mul(self, toExp(other)).simplify()

    def __rmul__(self, other):
        return Mul(toExp(other), self).simplify()

    def __truediv__(self, other): # self / other
        return TrueDiv(self, toExp(other)).simplify()

    def __rtruediv__(self, other):
        return TrueDiv(toExp(other), self).simplify()

    def __neg__(self):
        return Neg(self).simplify()

    def __pow__(self, power, modulo=None):
        return Pow(self,toExp(power)).simplify()

    def __rpow__(self, other):
        return Pow(toExp(other),self).simplify()

class Pow(Exp):
    def __init__(self,base,power):
        self.base = base
        self.power = power

    def simplify(self):
        if isinstance(self.power, Const):
            if self.power.value == 0:
                return Const(1)
            elif self.power.value == 1:
                return self.base
            elif isinstance(self.base,Const):
                return Const(self.base.value ** self.power.value)
        elif isinstance(self.base, Const) and (self.base.value in (0,1)):
            return self.base
        return self

    def eval(self, **value):
        return self.base.eval(**value) ** self.power.eval(**value)

    def deriv(self, x):
        u, v = self.base, self.power
        return self * v.deriv(x) * log(u) + v * u ** (v - 1) * u.deriv(x)

    def __repr__(self):
        return f"{self.base} ** {self.power}"

def log(value,base=math.e):
    return Log(value,Const(base)).simplify()

class Log(Exp):
    def __init__(self,value,base):
        self.value = value
        self.base = base

    def eval(self,**value):
        return math.log(self.value.eval(**value),self.base.eval(**value))

    def simplify(self):
        if isinstance(self.value,Const):
            if self.value.value == 1:
                return Const(0)
            if isinstance(self.base,Const):
                return Const(math.log(self.value.value,self.base.value))
        return self

    def deriv(self, x):
        u, v = self.value, self.base
        result = u.deriv(x) * log(v) / u - v.deriv(x) * log(u) / v
        return result / log(v) ** 2

    def __repr__(self):
        return f"log{self.base}({self.value})"

class Neg(Exp):
    def __init__(self,value):
        self.value = value

    def eval(self,**value):
        return -self.value.eval(**value)

    def simplify(self):
        if isinstance(self.value,Const):
            return Const(-self.value.value)
        return self

    def deriv(self, x):
        return -self.value.deriv(x)

def toExp(other):
    if isinstance(other,Exp):
        return other
    elif type(other) in (float,int):
        return Const(other)
    raise Exception(f"Can not convert {other} into Exp")

class Const(Exp): # 常量类
    def __init__(self,value):
        self.value = value

    def eval(self,**value):
        return self.value

    def deriv(self,x): # 导数
        return 0

    def __repr__(self):
        return str(self.value)

class Variable(Exp): # 变量类
    def __init__(self,name):
        self.name = name

    def eval(self,**value):
        if self.name in value:
            return value[self.name]
        raise Exception(f"Variable {self.name} is not fount")

    def deriv(self, x): # 导数
        value = ""
        if isinstance(x,Variable):
            value = x.name
        if type(x) == str:
            value = x
        return Const(1 if value == self.name else 0)

    def __repr__(self):
        return self.name

class Add(Exp):
    def __init__(self,left:Exp,right:Exp):
        self.left = left
        self.right = right

    def simplify(self):
        if isinstance(self.left,Const) and self.left.value == 0:
            return self.right
        elif isinstance(self.right,Const) and self.right.value == 0:
            return self.left
        elif isinstance(self.left,Const) and isinstance(self.right,Const):
            return Const(self.left.value + self.right.value)
        return self

    def eval(self,**value):
        return self.left.eval(**value) + self.right.eval(**value)

    def deriv(self, x):
        return self.left.deriv(x) + self.right.deriv(x)

    def __repr__(self):
        return f"{self.left} + {self.right}"

class Sub(Exp):
    def __init__(self,left:Exp,right:Exp):
        self.left = left
        self.right = right

    def simplify(self):
        if isinstance(self.left,Const) and self.left.value == 0:
            return -self.right
        elif isinstance(self.right,Const) and self.right.value == 0:
            return self.left
        elif isinstance(self.left,Const) and isinstance(self.right,Const):
            return Const(self.left.value - self.right.value)
        return self

    def eval(self, **value):
        return self.left.eval(**value) - self.right.eval(**value)

    def deriv(self, x):
        return self.left.deriv(x) - self.right.deriv(x)

    def __repr__(self):
        return f"{self.left} - {self.right}"

class Mul(Exp):
    def __init__(self,left:Exp,right:Exp):
        self.left = left
        self.right = right

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return Const(0)
            elif self.left.value == 1:
                return self.right
            elif isinstance(self.right, Const):
                return Const(self.left.value * self.right.value)
        elif isinstance(self.right, Const):
            if self.right.value == 0:
                return Const(0)
            elif self.right.value == 1:
                return self.left

        return self

    def eval(self, **value):
        return self.left.eval(**value) * self.right.eval(**value)

    def deriv(self, x):
        return self.left.deriv(x) * self.right + self.left * self.right.deriv(x)

    def __repr__(self):
        return f"{self.left} * {self.right}"

class TrueDiv(Exp):
    def __init__(self,left:Exp,right:Exp):
        self.left = left
        self.right = right

    def simplify(self):
        if isinstance(self.right,Const):
            if self.right.value == 0:
                raise Exception("0不能作除数！")
            elif self.right.value == 1:
                return self.left
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return Const(0)
            elif isinstance(self.right, Const):
                return Const(self.left.value / self.right.value)
        return self

    def eval(self, **value):
        return self.left.eval(**value) / self.right.eval(**value)

    def deriv(self, x):
        u,v = self.left,self.right
        return (u.deriv(x) * v - u * v.deriv(x)) / (v ** 2)

    def __repr__(self):
        return f"{self.left} / {self.right}"

def sin(value):
    return Sin(toExp(value)).simplify()

class Sin(Exp):
    def __init__(self,value):
        self.value = value

    def simplify(self):
        if isinstance(self.value,Const):
            return Const(math.sin(self.value.value))
        return self

    def eval(self, **value):
        return math.sin(self.value.eval(**value))

    def deriv(self, x):
        return cos(self.value) * self.value.deriv(x)

    def __repr__(self):
        return f"sin({self.value})"

def cos(value):
    return Cos(toExp(value)).simplify()

class Cos(Exp):
    def __init__(self,value):
        self.value = value

    def simplify(self):
        if isinstance(self.value,Const):
            return Const(math.cos(self.value.value))
        return self

    def eval(self, **value):
        return math.cos(self.value.eval(**value))

    def deriv(self, x):
        return -sin(self.value) * self.value.deriv(x)

    def __repr__(self):
        return f"cos({self.value})"

def tan(value):
    return Tan(toExp(value)).simplify()

class Tan(Exp):
    def __init__(self,value):
        self.value = value

    def simplify(self):
        if isinstance(self.value,Const):
            return Const(math.tan(self.value.value))
        return self

    def eval(self, **value):
        return math.tan(self.value.eval(**value))

    def deriv(self, x):
        return self.value.deriv / (cos(self.value) ** 2)

    def __repr__(self):
        return f"tan({self.value})"

def cot(value):
    return 1 / (Tan(toExp(value)).simplify())

if __name__ == '__main__':
    c1 = Const(1)
    c2 = Const(2)
    v1 = Variable("x")

    print(f"c1 = {c1} , c2 = {c2}")
    print(f"c1 + 10 = {c1 + 10}")
    print(f"c1 + v1 = {0 + v1}")
    print(f"c1 - c2 = {c1 - c2}")
    print(f"c1 * c2 = {c1 * v1}")
    print(f"c1 * 0 = {c1 * 0}")
    print(f"c1 / c2 = {c1 / c2}")

    c1 = Const(1)
    c2 = Const(12.345)

    x = Variable('x')
    y = Variable('y')

    a = (3 * x ** 5 + 4 * x + 12).deriv(x)
    print(a, '(x=0.5)=', a.eval(x=0.5))

    print((x ** 0.5).deriv(x))

    print(sin(math.pi / 2))

    print(cos(0))

    print(tan(math.pi / 4))

    print(cot(math.pi / 4))

    print((x ** 2 + y ** 2).deriv(y).eval(y=0.5))
