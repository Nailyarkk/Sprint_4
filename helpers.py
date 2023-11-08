import random

names = ["Алиса", "Лика", "Маша", "Пуговка", "Даша", "Галя", "Женя"]


def generate_random_name():
    return random.choice(names)


lastname = ["Иванова", "Ахматова", "Достоевская", "Васнецова", "Генадьева", "Чехова", "Каренина"]


def generate_random_lastname():
    return random.choice(lastname)


address = ["Москва", "Саратов", "Красноярс", "Казань", "Архангельск", "Барнаул", "Астрахань"]


def generate_random_address():
    return random.choice(address)


def generate_random_phone_number():
    country_code = "+7"
    area_code = str(random.randint(100, 999))
    first_part = str(random.randint(100, 999))
    second_part = str(random.randint(1000, 9999))

    phone_number = f"{country_code}{area_code}{first_part}{second_part}"
    return phone_number
