### 题目1:
阶乘：求阶乘100！，100的阶乘的结果数据很大，在其它语言(例如java)中根本无法直接计算，请设计一个方法计算100的阶乘，并保证该方法在各语言中能通用。
>提示：使用列表保存每一位数，使用字符串保存结果。

### 题目2:
五猴分桃：有五个猴子，分一堆桃；第一个猴子过来把桃分了5份，多出一个桃，它拿走了其中一份和多出来的一个桃；第二个猴子把剩下的桃再分了5份，也多出了一个桃，它像第一个猴子那样拿走了其中一份和多出来的一个桃；后面3个猴子也遇到了第一和第二个猴子的情况，也做出了同样的选择；问至少有多少个桃？


### 题目3:
扑克排序：有一组特定顺序的扑克共20张，扑克上有1-20的数字；将第一张扑克拿出来，上面显示多少的数字，就将接下来多少张扑克放到底部，然后再拿第二张扑克出来，第二张上面显示多少的数字，也将接下来多少张扑克放到底部......最终扑克全拿出来后显示的扑克顺序刚好是1、2、3、4......18、19、20.请问最初扑克的顺序是怎么样的？
>使用反推法，将上面的过程反推。

### 题目4
囚犯问题：有4个囚犯，分别独立关在4个房间，每天晚上随机一个人出来守夜，守夜的地方有一盏灯，守夜人每晚只能对灯进行一次操作(开/关)，房间里的囚犯可以看到灯的情况；请设计一个方案，确保有一个人知道每个人都出来守过夜。

### 题目5
猜姓：假设有一系列名字，例如：赵权孙武张邓林李王彭蓝黄梁方刘。请这些姓写在一些纸页上，让客户说出哪些纸页上有他的姓，由这些纸面你能准确说出客户的姓。请用尽量少的纸页设计一个方案。

### 题目8
实现一个函数，可以求出两个整数的最大公约数。

### 题目9
河内塔：使用代码实现河内塔游戏的过程。

### 题目10
实现斐波那契数列，能够找出第n位的数字。
>斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

### 题目20
牛顿法：使用牛顿法求解<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}" title="\sqrt{n}" />的值；

>设<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}&space;=&space;x" title="\sqrt{n} = x" />,那么 <img src="https://latex.codecogs.com/gif.latex?x^2&space;=&space;n" title="x^2 = n" />,设<img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;x^2" title="f(x) = x^2" />,那么该问题就是求函数f(x) = n时的正解；
>
>牛顿法：<img src="https://latex.codecogs.com/gif.latex?\frac{df(x)}{dx}&space;=&space;\dot{f(x)}" title="\frac{df(x)}{dx} = \dot{f(x)}" />,因此<img src="https://latex.codecogs.com/gif.latex?dx&space;=&space;\frac{d(f(x))}{\dot{f(x)}}" title="dx = \frac{d(f(x))}{\dot{f(x)}}" />,
>
>其中 df(x) = n - f(x) ， x -> x + dx

### 题目21
梯度下降法(GD1)：使用梯度下降法求解<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}" title="\sqrt{n}" />的值；

>梯度下降法(GD1)的求解原理跟牛顿法差不多，唯一不同的地方是dx公式不一样，梯度下降法(GD1)的x的梯度是<img src="https://latex.codecogs.com/gif.latex?dx&space;=&space;\gamma&space;*&space;df(x)&space;*&space;\dot{f(x)}" title="dx = \gamma * df(x) * \dot{f(x)}" />
>
>其中<img src="https://latex.codecogs.com/gif.latex?\gamma" title="\gamma" />是步长。

### 题目22
二分法求解<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}" title="\sqrt{n}" />的值；

>设<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}&space;=&space;x" title="\sqrt{n} = x" />,那么 <img src="https://latex.codecogs.com/gif.latex?x^2&space;=&space;n" title="x^2 = n" />,设<img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;x^2" title="f(x) = x^2" />,那么该问题就是求函数f(x) = n时的正解；
>
>先初始化x1、x2，确保f(x1) < n , f(x2) > n，使xm = (x1+x2)/2，判断f(xm)与n的大小关系，从而更新x1或x2的值，重复多次，直到f(xm)与n的误差在可接受的范围内。
>

### 题目23
梯度下降法(GD2)：使用梯度下降法求解<img src="https://latex.codecogs.com/gif.latex?\sqrt{n}" title="\sqrt{n}" />的值；梯度下降法(GD2)是在公式一的基础上做了优化，梯度中去掉了df(x),使得<img src="https://latex.codecogs.com/gif.latex?dx&space;=&space;\gamma&space;*&space;\dot{f(x))}" title="dx = \gamma * \dot{f(x))}" />因为少了df(x)，所以GD2不能求解特定值的解，而是求函数的最小值解，但可以改造原函数，使得其可以求解特定值的解。

>使 <img src="https://latex.codecogs.com/gif.latex?g(x)&space;=&space;(f(x)&space;-&space;n)^2" title="g(x) = (f(x) - n)^2" />,求g(x)的最小值解，即是求f(x) = n时的解
>

### 题目24
使用GD2求<img src="https://latex.codecogs.com/gif.latex?f(x1,x2)&space;=&space;(x1&space;-&space;3)^2&space;&plus;&space;(x2&space;&plus;&space;4)^2" title="f(x1,x2) = (x1 - 3)^2 + (x2 + 4)^2" />的最小值时的解。

### 题目25
GD1、GD2练习


