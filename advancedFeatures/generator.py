#生成器
g =(x*x for x in range(1,11))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


iter = iter([1,3,6,7,87])

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
try:
    next(iter)
    print("success")
except StopIteration:
    print("over")