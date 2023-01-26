# 迭代器的介绍
#   集合数据类型：list, tuple, dict, set, str等
#   generator是包括生成器和yield的generator function
#       可以被next()函数不断调用并返回下一个值，直至抛出StopIteration错误而无法返回下一个值
# 这些都可以作用于for循环，所以这些对象统称为可迭代对象：Iterable
# 可以用isinstance()来判断这个对象是否是iterable的。

from collections import Iterable, Iterator
print("List: ", isinstance([], Iterable))
print("String: ", isinstance('abc', Iterable))
print("Tuple: ", isinstance((), Iterable))
print("Dictionary: ", isinstance({}, Iterable))
print("Number: ", isinstance(100, Iterable))


# 可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterator
# 可以用isinstance()来判断这个对象是否是iterator的。
#   生成器都是Iterator对象
#   但是list, dict, str虽然是Iterable，却不是Iterator
    # 可以用iter()函数把list, dict, str等Iterable对象变成Iterator

print("迭代器：", isinstance( (x for x in range(10)), Iterator))

str = 'abc'
str_iterator = iter(str)    # 变成了迭代器
print(str_iterator.__next__())
print(str_iterator.__next__())
print(str_iterator.__next__())
print(str_iterator.__next__())
