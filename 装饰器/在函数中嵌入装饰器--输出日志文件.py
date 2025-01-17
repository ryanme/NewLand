# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/9 22:41

from functools import wraps

def logit(logfile='out.log'):
    def logging_decortor(func):
        @wraps(func)
        def wrapped_function(*argsl, **kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*argsl, **kwargs)
        return wrapped_function
    return logging_decortor



@logit()
def myfunc1():
    pass


myfunc1()   # Output: myfunc1 was called
            # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串


@logit(logfile='func2.log')
def myfunc2():
    pass


myfunc2()   # Output: myfunc2 was called
            # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串