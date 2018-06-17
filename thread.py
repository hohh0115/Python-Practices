import threading
import time
from queue import Queue

"""
# 基本使用
def thread_job():
    # for i in range(10):
    print(' this is the added_thread, number is %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    # 為何不會被算在下方的active_count()中? 因為thread_job()僅僅執行一條語句，
    # 若加上迴圈就會發現thread_job()和main()兩個都會跑
    # 若不是分成兩個線程去跑，會等迴圈跑完才回來main()之中
    print(threading.active_count())  # 現在有多少個thread正在運行
    # 詳列正在運行的thread身分，
    # 一定會有一個main thread: In normal conditions, the main thread is the thread from which the Python interpreter was started.
    print(threading.enumerate())
    print(threading.current_thread()) # 目前運行的是哪個thread

if __name__ == '__main__':
    main()
"""

"""
# join() 強制等待某線程執行完畢再回去執行main thread
def thread_job():

    # # 1
    # print('T1 starts\n')
    # # Suspend execution of the calling thread for the given number of seconds.
    # time.sleep(5)
    # print('T1 end\n')

    # 2
    for i in range(20):
        print(i)
        time.sleep(0.05)

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    added_thread.start()
    # Wait until the thread terminates.
    # This blocks the calling thread until the thread whose join() method is called terminates
    #  – either normally or through an unhandled exception – or until the optional timeout occurs.
    for i in range(50):
        if i == 20:
            added_thread.join()  # 這句使added_thread執行完後才執行下面的print('all done\n')
        print('main thread', i)

    print('all done\n')

if __name__ == '__main__':
    main()
"""

"""
# multithreading 練習
def square_it(list, queue):
    for i in range(len(list)):
        list[i] = list[i]**2
    # print(list)
    # Put item into the queue.
    # 其實改用串列去存也有同樣效果...
    queue.put(list)

def multithreading(data):
    q = Queue()
    threads = []
    for val in data:
        t = threading.Thread(target=square_it, args=(val, q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(len(data)):  # "_": ignore something
        results.append(q.get())  # Remove and return an item from the queue.

    print(results)

if __name__ == '__main__':
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    multithreading(data)
"""

"""
# 在python中用multithreading不一定快到哪裡
def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(list, multiplication_times):
    q = Queue()
    threads = []
    for _ in range(multiplication_times):
        t = threading.Thread(target=job, args=(list, q))
        t.start()
        threads.append(t)

    [thread.join() for thread in threads]
    total = 0
    for _ in range(multiplication_times):
        total += q.get()

    print(total)

def normal(list):
    print(sum(list))

if __name__ == '__main__':
    
    multiplication_times = 4

    l = list(range(100000))
    s_t = time.time()
    normal(l*multiplication_times)
    print('normal: ', time.time() - s_t)

    s_t = time.time()
    multithreading(l, multiplication_times)
    print('multithreading: ', time.time()-s_t)
"""

def job1():
    global A, lock
    # lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    # lock.release()

def job2():
    global A, lock
    # lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    # lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
