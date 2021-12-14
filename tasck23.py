# Укажите для словаря developer1 свое имя и город по соответствующим ключам
developer1 = {'Name': 'Сергей', 'City': 'Днепр', 'Skill': 'Python', 'Rate': 600, 'Phone': '+380631234573'}
developer2 = {'Name': 'Peter', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1800, 'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan', 'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex', 'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

developers_list = [developer1, developer2, developer3, developer4, developer5]


def get_rates(developers):
    developer_rates = []
    # Допишите эту функцию, которая получает список словарей с тинформацией о
    # разработчиках и возвращает список из зарплат
    for salary in developers:
        developer_rates.append(salary["Rate"])
    return developer_rates


print(get_rates(developers_list))