import logging


def exception01(a,b=0):
    result =0;
    try:
        print('trying....')
        result =a/b
    except ValueError as  e:
        print('except:',e)
        result = -2
    except ZeroDivisionError as e:
        print('except:',e)
        result =-1
    except Exception as e:
        # print("except:",e)
        logging.exception(e)
        return -3
    finally:
        print('finally block...')
    print('end')
    return result

if __name__ == '__main__':
    print(exception01(10,'e'))