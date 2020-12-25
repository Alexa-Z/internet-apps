import time


class cm_timer_1:

    def __enter__(self):
        self.time = time.time()

    def __exit__(self, value, key, traceback):
        print(time.time()-self.time)


class cm_timer_2:
    def __init__(self):
        self._start_time = None

    def __enter__(self):
        self._start_time = time.perf_counter()

    def __exit__(self, value, key, traceback):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        
with cm_timer_1():
    time.sleep(5.5)
with cm_timer_2():
    time.sleep(3.5)        