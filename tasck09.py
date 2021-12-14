# конкатенация ( + )
# Задание:
# Создайте три переменные: name, rate, my_qualification
name = "Сергей" # внесите свое имя
rate = 0 # внесите заработок
my_qualification = "junior"# квалификация в соответствии с зарплатой (rate)
# реализуйте необходимое количество операторов if, в результате которых
# переменная qualification получит значение в соответствии со значением
# rate и зарплатной политикой junior<1000, 1000<=middle<=2200, senior>2200.
if rate < 1000:
    qualification = "junior"
if rate >= 1000 and rate <= 2200:
    qualification = "middle"
if rate > 2200:
    qualification = "senior"
# В результатае віполнения задания (если ві бі введи имя Max и квалификацию junior)
# должна сформироватся строка My name is Max! I am the junior developer.


answer = "My name is "+name+"! I am the "+qualification+" developer."
print(answer)