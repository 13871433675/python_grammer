class Parent():
    pass


class Student(Parent):
    __doc__ = 'class doc test';

    def __init__(self, name, score):
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
        # 就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__name

    def print_score(self):
        print("%s,%s" % (self.get_name(), self.get_score()))

    def get_grade(self):
        if self.score > 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
#
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

if __name__ == '__main__':
    student = Student('qizhi', 35);
    student.print_score();
    print(student.get_name())
    # 强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
    # 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
    print(student._Student__name)
    print(Student.__doc__)
