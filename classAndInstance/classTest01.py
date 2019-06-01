# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，
# 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

class Parent():
    pass


class Student(Parent):
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s,%s" % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


if __name__ == '__main__':
    student = Student('qizhi', 35);
    student.name = 'wang'
    student.print_score();
    print(student.get_grade())
