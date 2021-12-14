# функции:
# min(список) - одно минимальное
# max(список) - одно максимальное
# len(список) - цифра, количество єлементов в списке
# sum(список) - сумма, значений всех єлементов в списке
# Задание, в mean среднее значение из rates
# в item_number количество элементов в rates
# в total сумме всех элементов rates
rates = [600, 800, 1800, 2500]

rates_min = min(rates)
rates_max = max(rates)
item_number = len(rates)
total = sum(rates)
mean = total / item_number
print(mean, total, item_number)