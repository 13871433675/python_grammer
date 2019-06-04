import json

__doc__='''

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''
class Student(object):
    def __init__ (self, name, age, score):
        self.name = name
        self.age = age
        self.score = score



if __name__ == '__main__':
    s =Student('wangqizhi',29,100)
    print(json.dumps(s,default=lambda obj: obj.__dict__))

    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)
    print(s)
