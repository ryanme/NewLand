### Python可迭代对象，迭代器，生成器的区别

---

```
          --> 迭代器 --> 生成器
可迭代对象 --> 序列(包括字符串，列表和元组)
          --> 字典
```

* 可迭代对象与迭代器
    * 可迭代对象包含迭代器。
    * 如果一个对象拥有__iter__方法，其是可迭代对象；如果一个对象拥有next方法，其是迭代器。
    * 定义可迭代对象，必须实现__iter__方法；定义迭代器，必须实现__iter__和next方法。

* 可以直接作用于for循环的对象统称为可迭代对象：Iterable。

* 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
   
* 一边循环一边计算的机制，称为生成器：generator。

* 生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。

* 生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，但是，不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器