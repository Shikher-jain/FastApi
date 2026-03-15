class Timer:
    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")

with Timer():
    print("Running task")