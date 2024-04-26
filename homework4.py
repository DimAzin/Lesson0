immutable_var = 1, True, "my_string"
print("Кортеж: ", immutable_var)

# immutable_var[0] = "2"
# TypeError: 'tuple' object does not support item assignment
# Кортеж не поддерживает изменение элементов

mutable_list = [1, True, "my_string"]
mutable_list[1] = "_false"
print("Измененный список: ", mutable_list)