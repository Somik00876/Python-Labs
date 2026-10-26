import sys

animals = {
    101: "Собачка",
    102: "Кошечка",
    103: "Хомячек"
}

key = 102
name = animals.get(key)
print(f"Поиск по ключу {key}: {name}\n")

my_range = range(5)

my_list = list(my_range)    #Список
my_tuple = tuple(my_range)  #Кортеж
my_set = set(my_range)      #Множество
my_dict = {i: str(i) for i in my_range}  #Словарь

print(f"Список (list):   {sys.getsizeof(my_list)} байт")
print(f"Кортеж (tuple):  {sys.getsizeof(my_tuple)} байт")
print(f"Множество (set): {sys.getsizeof(my_set)} байт")
print(f"Словарь (dict):  {sys.getsizeof(my_dict)} байт")