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

    with open("test.txt", 'w', encoding='utf-8', errors='ignore') as f:
        f.write("\n写入文件测试！")