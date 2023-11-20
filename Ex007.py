from random import randint
import threading
import multiprocessing
import asyncio
import time

arr = [randint(1,101) for _ in range(1000000)]
start_time = time.time()
sum = 0
# sum = multiprocessing.Value('i',0)

# def arr_sum(k):
# def arr_sum(k, cnt):
async def arr_sum(k):
    global arr
    global sum
    slice = int(len(arr)/4)
    small_arr = arr[slice*k:slice*(k+1)]
    for i in range(len(small_arr)):
        sum+=small_arr[i]
        # with cnt.get_lock():
            # cnt.value += small_arr[i]

def thr():
    threads = []
    for i in range(4):
        t = threading.Thread(target=arr_sum, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def proc():
    global sum
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=arr_sum, args=(i, sum,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

async def main():
    tasks = []
    for i in range(4):
        a = asyncio.create_task(arr_sum(i))
        tasks.append(a)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    # thr()
    # proc()
    asyncio.run(main())
    print(f'{time.time()-start_time:.2f}')
    print(sum)
    # print(sum.value)