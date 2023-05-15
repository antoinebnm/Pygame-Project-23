import time, sys

"""Time = []
Time.append(time.time())
time.sleep(1)
Time.append(int(time.time() - Time[0]-1))

print(Time[1])"""

#print("Version: "+'.'.join([str(x) for x in sys.version_info if x in [3,11]]))

from concurrent.futures import ThreadPoolExecutor

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor(max_workers=8) as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()
        
        executor.shutdown()

def funcA():
    print('Wait 4sec for A')
    for t in range(4):
        time.sleep(1)
        print("A:"+str(t+1))
    print("A")

def funcB():
    print('Wait 1sec for B')
    for t in range(1):
        time.sleep(1)
        print("B:"+str(t+1))
    print("B")


print(ThreadPoolExecutor()._max_workers)

for i in range (3):
    run_io_tasks_in_parallel([
    lambda: funcA(),
    lambda: funcB(),
])