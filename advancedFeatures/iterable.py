from collections import Iterable

# print(isinstance('abc',Iterable))
# print(isinstance(True,Iterable))
# print(isinstance(111,Iterable))
# print(isinstance((1,2,3),Iterable))
# print(isinstance([1,'3',44],Iterable))
# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)



# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not isinstance(L,Iterable):
        return "L is be Iterable"
    if len(L)==0:
        return (None,None)
    min =L[0]
    max =L[0]
    for i in L:
        if i <min:
            min=i
        elif i>max:
            max=i
    return (min,max)

if __name__ == '__main__':
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')