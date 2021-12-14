developer1 = {'Name': 'Vlad',  "City": "Kyiv", "Skill": "Python", "Rate": 1300, 'Phone': '+380631234570'}
developer2 = {'Name': 'Max',   "City": "Lviv", "Skill": "Python", "Rate": 1200, 'Phone': '+380631234571'}
developer3 = {'Name': 'Ivan',  "City": "Kyiv", "Skill": "Python", "Rate": 2800, 'Phone': '+380631234572'}
developer4 = {'Name': 'Anton',  "City": "Kyiv", "Skill": "Python", "Rate": 3800, 'Phone': '+380631234573'}
developer5 = {'Name': 'Alex',  "City": "Lviv", "Skill": "Python", "Rate": 4800, 'Phone': '+380631234574'}

developers = [developer1, developer2, developer3, developer4, developer5]
# В переменную sum_1_3_5 присвойте сумму заработных плат 1, 3 и 5 разработчика
# (помните, что у людей список начинается с 1, а в программировании - с 0).
# В переменную tel_5 присвойте значение номера телефона 5-го разрвботчика.
sum_1_3_5 = sum([developers[0]["Rate"], developers[2]["Rate"], developers[4]["Rate"]])
tel_5 = developers[4]["Phone"]
print(sum_1_3_5, tel_5)