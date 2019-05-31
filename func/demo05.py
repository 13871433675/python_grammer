#命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def  person(name,age,*,city,job):
    print(name,age,city,job)



if __name__ == '__main__':
    person('wangqizhi',30,city='wuhan',job='coder')