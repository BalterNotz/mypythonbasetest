#!/usr/bin/env python3
# Python3

'''exception的使用'''

file_name = input('请输入需要打开的文件名：')
f = None
try:
    f = open(file_name, encoding='utf-8')
    chs = f.read(10)
except (FileNotFoundError, FileExistsError) as e:
    print('文件没有找到: Exception: %s' % e)
    raise Exception('balabala1111')
except UnicodeDecodeError as e:
    print('文件解码发生错误：Exception: %s' % e)
    raise Exception('balabala2222')
except Exception as e:
    print(str(e))
else:
    f.close()
    print(chs)
finally:
    print('finally,不管是否发生异常都后都会执行。')
