class Animal():
    def run(self):
        print("animal is running!!")


class Dog(Animal):

    def run(self):
        super().run()
        print("Dog is running!!! wang wang wang ~~")


class Cat(Animal):
    pass

if __name__ == '__main__':
    dog = Dog();
    dog.run();

    a = list();
    b = Dog();
    c = Cat();

    print(isinstance(a,list))
    print(isinstance(b,Dog))
    print(isinstance(b,Animal))

    # 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()
    # 方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()
    # 方法，这就是多态的意思：
    #
    # 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()
    # 方法，而具体调用的run()
    # 方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()
    # 方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：


    # 静态语言
    # vs
    # 动态语言
    # 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()
    # 方法。
    #
    # 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()
    # 方法就可以了：
    #
    # class Timer(object):
    #     def run(self):
    #         print('Start...')
    #
    #
    # 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    #
    # Python的“file - like
    # object“就是一种鸭子类型。对真正的文件对象，它有一个read()
    # 方法，返回其内容。但是，许多对象，只要有read()
    # 方法，都被视为“file - like
    # object“。许多函数接收的参数就是“file - like
    # object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()
    # 方法的对象。
