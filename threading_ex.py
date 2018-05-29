# built-in


from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import time


def task(num):
    print("Executing Task")
    time.sleep(num)
    return num


executor = ThreadPoolExecutor(max_workers=3)
task1 = executor.submit(task, 2)
task2 = executor.submit(task, 5)
future_map = dict()
future_map[task1] = 2
future_map[task2] = 5

# as_completed(fs=sequence of futures)
for future in futures.as_completed(future_map):
    print(f"{future.result()} {future_map[future]}")
