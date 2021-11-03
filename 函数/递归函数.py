
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

fact(10)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(n, product):
    if n==1:
        return product
    return fact_iter(n-1, n*product)    

fact(10)
#

