# coding: utf8
"""
实例化class，直接class.func_name得到属性，不加()
"""


class StudentInfo:
    def __init__(self, sex=None, age=None):
        self._sex = sex
        self._age = age

    @property
    def sex(self):
        return self._sex

    @property
    def age(self):
        return self._age


S = StudentInfo('男', 18)
print(S.age)
print(S.sex)