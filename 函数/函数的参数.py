

def calc(*nums):
    all_num = 0
    for num in nums:
        all_num += num
    print("all_num: ", all_num)

nums_1 = [1,2,3,4,5]
calc(*nums_1)

def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'kw: ', kw)

#person("huajia", 27)
#person("huajia", 27, ciy='zhuhai', qu='hengqing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("huajia", 27, **extra)

def person(name, age, *, city, job):
    print(name, age, city, job)

person("huajia", 27, guojia = 'Beijing', job = 'Engineer')    

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, city = 'Beijing', job = 'Engineer')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')    

def f1(a,b,c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# >>> f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
# >>> f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
# >>> f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# >>> f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# >>> f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


## 注意： 必选参数，默认参数，可变参数，命名关键字参数，关键字参数
# 可变参数 *nums
# * 在前面，还有**kw 
