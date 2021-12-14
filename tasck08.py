# and - И, or - ИЛИ
rate = 1800 # присвоить значение между 1000 и 2700 вкллючительно и первого и второго

if rate < 1000:
    qualification = 'junior'
if rate >= 1000 and rate <= 2700: # вписать условие
    qualification = 'middle' # сгенерировать соответствующий код
if rate > 2700: # вписать условие
    qualification = 'senior'

print(qualification)