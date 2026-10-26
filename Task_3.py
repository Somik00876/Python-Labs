import timeit

sizes = (1000, 10000, 100000)

print(f"{'Размер':<10} | {'Поиск в списке (Есть)':<22} | {'Поиск в списке (Нет)':<22} | {'Поиск в сете (Есть)':<22} | {'Поиск в сете (Нет)':<22}")
print("-" * 105)

for size in sizes:
    my_list = list(range(size))
    my_set = set(my_list)

    yes = size // 2
    no = -1

    list_yes = timeit.timeit(lambda: yes in my_list, number = 1000)
    list_no = timeit.timeit(lambda: no in my_list, number = 1000)
    set_yes = timeit.timeit(lambda: yes in my_set, number = 1000)
    set_no = timeit.timeit(lambda: no in my_set, number = 1000)

    '''print('1)',list_yes,'\n')
    print('2)',list_no,'\n')
    print('3)',set_yes,'\n')
    print('4)',set_no)'''
    print(f"{size:<10} | {list_yes:<22.6f} | {list_no:<22.6f} | {set_yes:<22.6f} | {set_no:<22.6f}")