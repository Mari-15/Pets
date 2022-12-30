import random


def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False


number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!')
print('Введите любое целое число от 1 до 100.')
flag = False
count = 0

while not flag:
    number_user = input()
    if not is_valid(number_user):
        print('А может быть все-таки введем целое число от 1 до 100?')
        number_user = input()
    number_user = int(number_user)
    if number_user < number:
        print('Ваше число меньше загаданного, попробуйте еще разок.')
        count += 1
    elif number_user > number:
        print('Ваше число больше загаданного, попробуйте еще разок.')
        count += 1
    elif number == number_user:
        count += 1
        print('Вы угадали, поздравляем!')
        print(f'Вы сделали {count} попыток.')
        count = 0
        print()
        print('Хотите сыграть еще? Нажмите "д" для "да" и "н" для "нет".')
        unswer = input()
        flag_2 = False
        while not flag_2:
            if unswer.lower() == 'д':
                number = random.randint(1, 100)
                print('Играем еще раз!')
                print('Мы задумали новое число. Дерзайте!')
                flag_2 = True
            elif unswer.lower() != 'н':
                print('Вы ввели что-то непонятное. Попробуйте еще раз.')
                unswer = input()
            elif unswer.lower() == 'н':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                flag = True
                break

