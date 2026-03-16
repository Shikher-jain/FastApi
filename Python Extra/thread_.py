import threading
import time
from concurrent.futures import ThreadPoolExecutor

def worker(num,num2):
    print(f'Thread {num} with value {num2} starting')
    time.sleep(2)
    print(f'Thread {num} with value {num2} finished')

with ThreadPoolExecutor(max_workers=500) as executor:
    futures = []
    for i in range(1000):
        future = executor.submit(worker, i, i*2)
        futures.append(future)

    for future in futures:
        future.result()

print("All threads completed")

