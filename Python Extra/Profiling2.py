import numpy as np
import cProfile

def slow_function():
    total = 0
    for i in range(10_000_000):
        total += i

def fast_function():
    total = sum(range(10_000_000))

def numpy_function():
    arr = np.arange(10_000_000)
    total = np.sum(arr)

def main():
    slow_function()
    fast_function()
    numpy_function()

cProfile.run("main()")