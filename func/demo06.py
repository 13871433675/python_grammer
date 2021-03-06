#递归函数
# def fact(n):
#     if(n==1):
#         return 1
#     return n * fact(n-1)
#
# print(fact(5))
# print(fact(1500)) 会导致栈帧溢出

# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：

# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的

def fact_iter(n, param):
    if n==1:
        return param
    return fact_iter(n-1,param*n)


def fact(n):
    return fact_iter(n,1)

print(fact(1500))

# 小结
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。