# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

'''  jhgjgghg
lkljh
kjhkjhkj
'''
def is_odd(n):
    return n%2==1

def not_empty(n):
    return len(n)>6;


print(list(filter(not_empty,["  ","111   ","eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"])))

