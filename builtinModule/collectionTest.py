# collection测试
import collections;

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

    # deque:解决list线性存储，数据量大的时候，插入和删除效率低下的问题
