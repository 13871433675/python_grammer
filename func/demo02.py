def add_end(L=()):
    if len(L)==0:
        L=[]
    L.append('END')
    return L

if __name__ == '__main__':
    print(add_end())
    print(add_end())
    print(add_end())

# 原因解释如下：
#
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#
#  定义默认参数要牢记一点：默认参数必须指向不变对象！
# Python的每个对象都分为可变和不可变，主要的核心类型中，数字、字符串、元组是不可变的，列表、字典是可变的。

