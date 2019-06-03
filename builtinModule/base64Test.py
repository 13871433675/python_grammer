import base64
from urllib import request

if __name__ == '__main__':
   print( base64.b64decode(b'binary\x00string') )
   print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

   with request.urlopen('https://www.baidu.com') as f:
       data = f.read()
       print('Status:', f.status, f.reason)
       for k, v in f.getheaders():
           print('%s: %s' % (k, v))
       print('Data:', data.decode('utf-8'))