

from typing import Iterable


L = list(range(100))
L[::-10]

d = {'a':1, 'b':2, 'c':3}

for key in d:
    print(key)

for key, value in d.items():
    print(key)
    print(value)

from collections.abc import Iterable

isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)
isinstance(123, Iterable)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    elif len(L)==1:
        return (L[0], L[0])
    else:
        return (min(L), max(L))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] 

[x if x%2==0 else 1 for x in range(1, 11)]
#[x if x % 2 == 0 for x in range(1, 11)]
# for 前面的部分是一个表达式，必须根据x计算出一个结果，不能没有结果
# 但是for 后面的if是过滤条件，不能带else

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) ]
