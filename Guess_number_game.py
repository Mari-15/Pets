import random


def is_valid(text, right):
    if text.isdigit() and 1 <= int(text) <= right:
        return True
    else:
        return False


right = 100
number = random.randint(1, right)
print('Добро пожаловать в числовую угадайку! Введи свое имя, Игрок!')
user_name = input()
print('Если захочешь остановиться - напиши "стоп".')
print()
print(f'{user_name.title()}, введите любое целое число от 1 до {right}.')
flag = False
count = 0

while not flag or number_user.lower() != 'стоп':
    number_user = input()
    if number_user.lower() == 'стоп':
        print(f'{user_name.title()}, поиграем в другой раз. Еще увидимся...')
        break
    elif not is_valid(number_user, right) and number_user.lower() != 'стоп':
        print(f'{user_name.title()}, a может быть все-таки введем '
              f'целое число от 1 до {right}?')
        number_user = input()
    if int(number_user) < number:
        print(f'Ваше число меньше загаданного, '
              f'попробуйте еще разок.')
        count += 1
    elif int(number_user) > number:
        print(f'Ваше число больше загаданного, '
              f'попробуйте еще разок.')
        count += 1
    elif number == int(number_user):
        count += 1
        print(f'{user_name.title()}, Вы угадали, поздравляем!')
        print(f'Вы сделали {count} попыток.')
        count = 0
        print()
        print(f'{user_name.title()}, хотите сыграть еще? '
              'Нажмите "д" для "да" и "н" для "нет".')
        unswer = input()
        flag_2 = False
        while not flag_2:
            if unswer.lower() == 'д':
                print(f'{user_name.title()}, хотите сменить правую границу? '
                      'Нажмите "д" для "да" и "н" для "нет".')
                unswer_right = input()
                flag_3 = False
                while not flag_3:
                    if unswer_right.lower() == 'д':
                        right = int(input('Введите число: '))
                        flag_3 = True
                    elif unswer_right.lower() == 'н':
                        break
                    else:
                        print('Вы ввели что-то непонятное. '
                              'Попробуйте еще раз.')
                        unswer_right = input()
                number = random.randint(1, right)
                print(f'Играем еще раз, {user_name.title()}!')
                print(f'Мы задумали новое число от 1 до {right}. Дерзайте!')
                flag_2 = True
            elif unswer.lower() != 'н':
                print('Вы ввели что-то непонятное. Попробуйте еще раз.')
                unswer = input()
            elif unswer.lower() == 'н':
                print(f'{user_name.title()}, спасибо, что играли в числовую угадайку. Еще увидимся...')
                flag = True
                break

