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

while not flag:
    number_user = input()
    if not is_valid(number_user):
        print('А может быть все-таки введем целое число от 1 до 100?')
        number_user = input()
    number_user = int(number_user)
    if number == number_user:
        print('Поздравляем, вы угадали!')
        flag = True
        break
    else:
        print('К сожалению, не правильно. Попробуйте еще!')

