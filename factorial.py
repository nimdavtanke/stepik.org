num = int(input('Введите число: '))
count = 1
fact = 1

while count <= num:
    fact = fact * count
    count += 1
print("Факториал числа", num, "равен:", fact)
