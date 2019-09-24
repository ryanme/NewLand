import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return t

    def now2(self):
        t = time.localtime()
        return t


a = Date('2019', 4, 22)
print(a.now())
print(a.now2())
print(Date.now())  # 不实例化直接调用
