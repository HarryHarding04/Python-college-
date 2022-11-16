import time


print("enter your name: ", end=" ")
start_time = time.process_time()
name = input()
elapsed = time.perf_counter() - start_time
print("it took you ", elapsed, "seconds to respond")
