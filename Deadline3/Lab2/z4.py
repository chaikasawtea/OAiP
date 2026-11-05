def my_range(start, end, step):
    while start < end:
        yield start
        start = start + step
for i in my_range(1, 3, 0.5):
    print(i)