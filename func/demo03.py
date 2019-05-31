#可变参数

def calc(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    return sum

if __name__ == '__main__':
    print(calc(1,2,3,4,66))

    numList =[7,5,7]
    print(calc(*numList))