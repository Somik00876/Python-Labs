import timeit
import gc

def rabbit():

    data = list(range(100_000))
 
    append = data.append
    pop = data.pop

    append(100_000)
 
    total = sum(data)
    
    found = (data[0] == 0)
    
    pop()

gc.disable()
rec_time = timeit.timeit(rabbit, number=1)
gc.enable()

print(f"Время выполнения кролика: {rec_time:.6f} сек.")
