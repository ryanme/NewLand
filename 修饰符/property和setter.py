# coding: utf8
"""
class中setter用法
"""


class StudentInfo:
    def __init__(self, sex=None, age=None):
        self._sex = sex
        self._age = age

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


S = StudentInfo()
S.sex = '男'
S.age = 18
print(S.age)
print(S.sex)
