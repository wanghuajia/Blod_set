def not_empty(s):
    return s and s.strip()#这个逻辑不理解

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break        

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)



def createCounter():
    fs = []
    def counter(i):
        def neibu():
            return i
        return neibu
    for i in range(2):
        fs.append(counter(i))
    return fs

f1, f2 = createCounter()
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

def is_odd(n):
    return n % 2 == 0

L = list(filter(lambda x:x%2==0, range(1, 20)))
