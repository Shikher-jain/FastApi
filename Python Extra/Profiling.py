import cProfile

def slow_function():
    total = 0
    for i in range(10_000_000):
        total += i
        # print(total)

def fast_function():
    total = sum(range(10_000_000))

def main():
    slow_function()
    fast_function()

    
cProfile.run("slow_function()")
cProfile.run("fast_function()")
cProfile.run("main()")