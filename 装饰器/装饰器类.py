# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/10 0:05

"""
除了方法，类也可以用来构建装饰器
"""

from functools import wraps


# 有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。
# 这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

class logit(object):
    def __init__(self, logfile='类.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


# 这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：
@logit()
def myfunc1():
    pass

myfunc1()


"""
现在，我们给 logit 创建子类，来添加 email 的功能(虽然 email 这个话题不会在这里展开)。
"""


class email_logit(logit):   # 类的继承
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email  # 子类新增参数
        super(email_logit, self).__init__(*args, **kwargs)  # 声明基类

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass

# 从现在起，@email_logit 将会和 @logit 产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。