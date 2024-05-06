#2.
# На вход программы подается 3 целых числа.
# Напишите программу, которая находит серединное значение из этих чисел
#
# a,b,c = 67, 100, 54
# result —> 67

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a == b or a == c:
    average = a
elif b == c:
    average = b
elif a < b and b < c or c < b and b < a:
    average = b
elif b < a and a < c or c < a and a < b:
    average = a
elif b < c and c < a or a < c and c < b:
    average = c

print(average)



