import time 
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        excu_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {excu_time:.4f} сек")
        return result
    return wrapper
@timer
def slow_func():
    # имитация долгой работы
    for _ in range(1000000): 
        pass 

slow_func()