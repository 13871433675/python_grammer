import json


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