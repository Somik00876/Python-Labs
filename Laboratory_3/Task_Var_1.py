conference_info = ("Python в инженерных задачах", "15.10.2026", 204)

application_list = [102, 117, 131, 145, 156, 160]

registered_set = {102, 117, 131, 145}

participants_dist = {
    102: "Анна Орлова",
    117: "Иван Петров",
    131: "Пал Лаич",  
    145: "Мистер Фриман"
}


print(f"Параметры конференции: «{conference_info[0]}», {conference_info[1]}, аудитория {conference_info[2]}")

apps_str = ", ".join(map(str, application_list))
print(f"Заявки в порядке поступления: {apps_str}")

reg_str = ", ".join(map(str, sorted(registered_set)))
print(f"Зарегистрированные участники: {reg_str}")


participants_str = " ; ".join([f"{k} - {v}" for k, v in participants_dist.items()])
print(f"Участники: {participants_str}")


new_application_id = 174
application_list.append(new_application_id)
apps_after_str = ", ".join(map(str, application_list))
print(f"\nПосле добавления заявки: {apps_after_str} ")

check_id = 131
is_registered = "да" if check_id in registered_set else "нет"
print(f"Участник {check_id} зарегистрирован: {is_registered}")

search_id = 117
fio_result = participants_dist.get(search_id, "Участник не найден")
print(f"ФИО участника {search_id}: {fio_result}")
