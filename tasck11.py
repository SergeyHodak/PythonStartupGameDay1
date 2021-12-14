# присвойте переменной string строку 0 1 2 3 4 5 6 7 8 9 10
# (после числа 10, как и после остальных, идет пробел)
string = ''
for i in range(11):
    string += str(i) + " "
print(string)
