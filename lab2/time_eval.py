from typing import Callable, List
from time import perf_counter, time, process_time

def time_eval(func: Callable, args: List, name="", times=10, print_res=False):
    """
    :param func: function to evaluate based on {@param times} runs
    :param args: func arguments
    :param name: function name
    :param print_res: if true, prints first result
    :return: result of func(args)
    """
    start_pc = perf_counter()
    start_t = time()
    start_pt = process_time()
    res = []
    for i in range(times):
        res = func(*args)
    end_pt = process_time()
    end_t = time()
    end_pc = perf_counter()
    avg_pc = (end_pc-start_pc)/times
    avg_t = (end_t-start_t)/times
    avg_pt = (end_pt-start_pt)/times
    if print_res:
        print(res[0])
    print(name, " running time actual: ", avg_t)
    print("process time: ", avg_pt)
    print("user time: ", avg_pc)
    return res
