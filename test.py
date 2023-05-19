import time, sys
from config import *

"""Time = []
Time.append(time.time())
time.sleep(1)
Time.append(int(time.time() - Time[0]-1))

print(Time[1])"""

#print("Version: "+'.'.join([str(x) for x in sys.version_info if x in [3,11]]))

"""from concurrent.futures import ThreadPoolExecutor

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
    funcA()
    print("B")


print(ThreadPoolExecutor()._max_workers)


run_io_tasks_in_parallel([
    lambda: funcA(),
    lambda: funcB()
])



import multiprocessing
from concurrent.futures import ThreadPoolExecutor

def event(stop_event):
    while not stop_event.is_set():
        print("Event")
        time.sleep(1)
        # Handle events or user input here
        # Add your event handling logic
        pass

def update(stop_event):
    while not stop_event.is_set():
        print("Update")
        time.sleep(1)
        # Update game state here
        # Add your game update logic
        pass

def game_core(stop_event, condition):
    while not stop_event.is_set():
        print('Game Core')
        # Game core logic here
        # Add your game logic and main gameplay loop

        # Check for game over condition
        if condition:
            stop_event.set()

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        stop_event = manager.Event()
        condition_met = False  # Initial value of the condition

        with multiprocessing.Pool() as pool:
            executor = ThreadPoolExecutor()

            # Execute event() and update() using ThreadPoolExecutor
            future_event = executor.submit(event, stop_event)
            future_update = executor.submit(update, stop_event)

            # Execute game_core using multiprocessing
            process_core = pool.apply_async(game_core, (stop_event, condition_met))

            # Wait for a keypress to stop the game
            input('Wait for Entrer : \n')
            condition_met = True  # Modify the condition to stop the game
            stop_event.set()

            # Wait for all tasks to complete
            future_event.result()
            future_update.result()
            process_core.get()
"""
