import logging

from click import File

if __name__ == '__main__':
    # # 获取已定义的对象字典
    # print(dir(vars()))
    # print(help(vars()))
    # try:
    #     f = open("test.txt",'r')
    #     print(f.read())
    # except FileNotFoundError as e:
    #     logging.exception(e)
    #     print("expect",e)
    # finally:
    #     if(vars().__contains__('f')):
    #         f.close()
    #         print("close success!")
    #     print("end")
    with open("test.txt",'r',encoding='utf-8',errors='ignore') as f:
        # line = f.read()
        # print(line)
        # print(f.readlines())  把每一行当作一个元素，生成一个数组，换行符也带着
        for line  in f.readlines():
            print(line.strip())#去掉换行
        if (f):
            f.close();
            print("file closed!")

    # read() readlines() readline()的区别
    # read()—当成一个字符串读出
    # readlines()readlines返回的是列表
    # readline()一行一行读文件
    # 如果文件很大，用read（）内存不够（如运维日志几十G）
    # 用readline来读超大文件
    # 原则：内存在电脑中是个稀缺的资源，如果你占用大量内存，程序肯定不是最优的，小文件：read、readlines速度更快些

    # 关于open()的mode参数：
    # 'r'：读
    # 'w'：写
    # 'a'：追加
    # 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
    # 'w+' == w+r（可读可写，文件若不存在就创建）
    # 'a+' ==a+r（可追加可写，文件若不存在就创建）
    # 对应的，如果是二进制文件，就都加一个b就好啦：
    # 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
    with open("test.txt", 'a', encoding='utf-8', errors='ignore') as f:
        f.write("\n写入文件测试！")