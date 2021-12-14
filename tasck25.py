# Укажите для словаря developer1 свое имя и город в соответствующие ключи
developer1 = {'Name': 'Сергей', 'City': 'Днепр', 'Skill': 'Python', 'Rate': 600, 'Phone': '+380631234573'}
developer2 = {'Name': 'Peter', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1800, 'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex', 'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

devs = [developer1, developer2, developer3, developer4, developer5]


def get_rate_stat(developers):
    # 1. Создайте пустой список rates.
    # 2. Создайте словарь stat с полями "mean", "min", "max": (со значениями None) и поля
    # "item_number" со значекниями 0.
    # 3. Из значений полей "Rate" списка словарей develops заполните созданный список rates.
    # 4. Обновите значение словаря stat:
    # ключ "mean" - среднее значение спеиска rates
    # min - минимальное из rates
    # max - максимальное из rates
    # item_number - количество элементов в списке rates
    # 5. Функция get_rate_stat возвращает stat.

    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    for rate in developers:
        rates.append(rate["Rate"])
    stat.update(
        {
            "mean": sum(rates) / len(rates),
            "min": min(rates),
            "max": max(rates),
            "item_number": len(rates)
        }
    )
    return stat

print(get_rate_stat(devs))