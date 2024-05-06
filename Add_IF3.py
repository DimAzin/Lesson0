# 3.
# Красный, синий и желтый называются основными цветами,
# потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
#  -если смешать красный и синий, то получится фиолетовый;
#  -если смешать красный и желтый, то получится оранжевый;
#  -если смешать синий и желтый, то получится зеленый.
#
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета,
# который получится в результате.

tuple_color = ('красный', 'синий', 'желтый')
color1 = input('Введите цвет1: ')

if color1 in tuple_color:
    color2 = input('Введите цвет2: ')
    if color2 in tuple_color:
        if (color1 == 'красный' and color2 == 'синий') or (color2 == 'красный' and color1 == 'синий'):
            print('фиолетовый')
        if (color1 == 'красный' and color2 == 'желтый') or (color2 == 'красный' and color1 == 'желтый'):
            print('оранжевый')
        if (color1 == 'желтый' and color2 == 'синий') or (color2 == 'желтый' and color1 == 'синий'):
            print('зеленый')
    else:
        print('Неправильно введен цвет2!')
else:
    print('Неправильно введен цвет1!')
