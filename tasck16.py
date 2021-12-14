developer_rates = [600, 800, 1800, 2500, 3300]
# присвойте перемееной total_juniors значение суммы зарплат всех
# junior-разработчиков, если известно, что их уровень оплаты
# менее 1000 долларов в месяц
# используйте при этом оператор not
total_juniors = 0
for rate in developer_rates:
    if not rate > 1000:
        total_juniors += rate
print(total_juniors)
