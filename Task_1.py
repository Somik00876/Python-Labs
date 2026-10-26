my_list = [10, 20, 30, 40, 50, 60]
my_tuple = (10, 20, 30, 40, 50, 60)
print('--- Исзодные данные ---')
print(f"Список: {my_list}, Тип: {type(my_list)}, ID: {id(my_list)}")
print(f"Кортеж: {my_tuple}, Тип: {type(my_tuple)}, ID: {id(my_tuple)}")

id_list_before = id(my_list)
my_list[0] = 99
id_list_after = id(my_list)
print('\n--- Изменение списка ---')
print(f"Новый список: {my_list}")
print(f"ID до изменения: {id_list_before}")
print(f"ID после изменения: {id_list_after}")

id_tuple = id(my_tuple)
my_tuple_new = (99, 20, 30, 40, 50, 60)
id_tuple_new = id(my_tuple_new)

print("\n--- Изменение кортежа ---")
print(f"Старый кортеж: {my_tuple}")
print(f"Новый кортеж:  {my_tuple_new}")
print(f"ID старого кортежа: {id_tuple}")
print(f"ID нового кортежа:  {id_tuple_new}")
