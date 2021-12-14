rates = [600, 800, 1800, 2500]
stat = {"mean": None, "min": None, "max": None, "item_number": 0, "total": 0}


stat["mean"] = sum(rates)/len(rates)
# в словарь stat по ключу min внесите минимальное значение заработной платы разработчиков из списка rates
stat["min"] = min(rates)
# в stat по max максимальное из rate
stat["max"] = max(rates)
# в stat по item_number количество элементов из rate
stat["item_number"] = len(rates)
# в stat по total сумма элементов из rate
stat["total"] = sum(rates)
print(stat)