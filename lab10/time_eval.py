from typing import Callable
from time import perf_counter

def time_eval(func: Callable, name, times,  *args, **kwargs):
    start_pc = perf_counter()
    res = []
    for i in range(times):
        res = func(*args, **kwargs)
    end_pc = perf_counter()
    avg_pc = (end_pc-start_pc)/times
    if name is not None:
        print(name, "time:", round(avg_pc, 6))
    return avg_pc, res