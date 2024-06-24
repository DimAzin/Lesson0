def add_everything_up(in_a, in_b):
    sum = None
    try:
        a = int(in_a)
    except:
        try:
            a = float(in_a)
        except:
            a = in_a

    if not (isinstance(a, str)):
        try:
            b = int(in_b)
        except:
            try:
                b = float(in_b)
            except:
                a = in_a
                b = in_b
    else:
        b = in_b

    sum = a + b
    return sum



in_a = input("Введите значение а:")
in_b = input("Введите значение b:")

print(f'Результат {add_everything_up(in_a, in_b)}')

