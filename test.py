import time, sys

"""Time = []
Time.append(time.time())
time.sleep(1)
Time.append(int(time.time() - Time[0]-1))

print(Time[1])"""

#print("Version: "+'.'.join([str(x) for x in sys.version_info if x in [3,11]]))

from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()

def funcA():
    time.sleep(3)
    print("A")

def funcB():
    time.sleep(1)
    print("B")

run_io_tasks_in_parallel([
    lambda: funcA(),
    lambda: funcB(),
])