"""
4) Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
n = int(input("Введите целое положительное число "))
max_number = n % 10
while n > 0:
    n = n // 10
    if n % 10 > max_number:
        max_number = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_number)
        break
