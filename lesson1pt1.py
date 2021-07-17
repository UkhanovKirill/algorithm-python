number = input('Введите трехзначное число: ')

summa = 0
prod = 1

for f in number:
    summa += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {summa}")
print(f"Произведение цифр: {number}: {prod}")