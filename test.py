import time

Time = []
Time.append(time.time())
time.sleep(1)
Time.append(int(time.time() - Time[0]-1))

print(Time[1])