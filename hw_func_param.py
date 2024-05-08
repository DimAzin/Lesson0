def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('A')
print_params(2, 6)
print_params('3', 6, '5')

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['a', 5, False]
values_dict = {'a':'A', 'b':3, 'c':True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'ff']
print_params(*values_list_2, 42)