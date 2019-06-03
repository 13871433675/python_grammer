import json
import pickle

if __name__ == '__main__':
    d = dict(name='Bob', age=20, score=88)
    # print(d)
    # f =open('test2.txt','wb')
    # pickle.dump(d,f)
    # print(d)
    # f =open('test2.txt','rb')
    # d =pickle.load(f)
    # print(d)

    print(type(json.dumps(d)))
