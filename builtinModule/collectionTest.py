# collection测试
import collections;
from collections import deque, defaultdict, OrderedDict

if __name__ == '__main__':
    p = (1, 2);
    # namedtuple提供了一个自定义的tuple的方法  namedtuple('名称',[属性list])
    Point = collections.namedtuple('Point', ['x', 'y'])
    point = Point(1, 2)
    print(point.x)
    print(point.y)
    print(isinstance(point, Point))

    Cicle = collections.namedtuple('Cicle', ['x', 'y', 'r'])
    cicle = Cicle(2, 3, 1);

    # deque:解决list线性存储，数据量大的时候，插入和删除效率低下的问题，为了高效时间插入和删除操作的双向列表，使用于队列和栈
    # deque除了实现list的append()和pop() 外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
    q = deque([x for x in 'abc'])
    q.append('qizhi')
    print(type(q))
    print(q)

    # defaultdict
    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
    # 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
    dic = {'x': 1, 'y': 2}
    # dic['z'] KeyError
    dic2 = defaultdict(lambda: 'defaultvalue')
    print(dic2['abc'])
    print('a' * 2)
    dic3 = {x: x * 2 for x in 'abc'}
    print(dic3)

    # 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    # 如果要保持Key的顺序，可以用OrderedDict, 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
    od = OrderedDict()
    od['z'] = 1
    od['y'] = 2
    od['a'] = 3
    od['z'] = 3  # 覆盖了首先插入的z的值，但是顺序还是没有变化
    print(list(od.items()))

