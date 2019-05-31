# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
from functools import reduce


def f(x,y):
    return x*y

# print(list(map(f,'wangqizhi')))
# print(list(map(f,[1,2,3,4,'wangqizhi'])))


# print(list(map(type,[1,'wangqizhi',[],True,None])))
# print(type(map(type,[1,'wangqizhi',[],True,None])))

for x in list(map(type,[1,'wangqizhi',[],True,None])):
    print(x)



# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

print("---------reduce test -----------")

print(reduce(f,[2,2,3]))

print("1.-------------------")
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：




