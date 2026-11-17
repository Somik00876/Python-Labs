import timeit

def turtle():
    data = []
    for i in range(100_000):
        element = f"item_number_{i}_"
        data = data[:] + [element]

    center = len(data) // 2
    data = data[:center] + ["new_element"] + data[center:]

    total_len = 0
    for item in data:
        idx = data.index(item)
        total_len += len(data[idx])

    target = "not_element"
    found = False
    for i in range(len(data)):
        if data[i] == target:
            found = True

    del data[len(data) // 2]

rec_time = timeit.timeit(turtle, number=1)
print(f"Время выполнения черепахи: {rec_time:.6f} сек.")
