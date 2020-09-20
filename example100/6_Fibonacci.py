# -*- encoding: utf-8 -*-
"""
@File    : 6_Fibonacci.py
@Time    : 2019/11/17 18:48
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
-------------------------------------
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
"""


def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


print(fib(10))


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(10))


def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(fib3(10))
