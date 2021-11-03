from multiprocessing import Pool
import time
import multiprocessing
 
def func(i):
    return  i*i
 

if __name__ == "__main__":
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    pool = multiprocessing.Pool(processes=8) # 创建4个进程
    results = []
    length = 5000
    for i in range(8):
        results.append(pool.apply_async(func, (i,)))
    pool.close() # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    pool.join() # 等待进程池中的所有进程执行完毕
    print ("Sub-process(es) done.")
    k = 0
    for res in results: 
        print(res.get())      
        k += res.get()
    print(k)
