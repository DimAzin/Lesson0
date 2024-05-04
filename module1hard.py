# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

dict_students = dict()
list_students = list(students)
list_students.sort()

for i in range(len(list_students)):
    average = 0
    for j in range(len(grades[i])):
        average = average + grades[i][j]

    average = average / len(grades[i])
    dict_students[list_students[i]] = average

print(dict_students)