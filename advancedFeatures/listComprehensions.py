import os

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(1,10)))

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2 ==0])

print([m+n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('../')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([ x +'='+y for x,y in d.items() ])

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]

print([x for x in L1  if isinstance(x,str)])
