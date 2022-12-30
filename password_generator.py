import random


def generate_password(length, char):
    return random.sample(char, length)


def generate_chars(list_yes):
    text = ''
    for i in range(len(list_yes)):
        if list_yes[i] == 'да':
            text += chars[i]
    return text


def is_digital_valid(number):
    if number.isalpha():
        return False
    else:
        return True


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
spec_symbols = 'il1Lo0O'

chars = [digits, lowercase_letters, uppercase_letters, punctuation, spec_symbols]

amount_passwords = input('Сколько нужно сгенерировать паролей? Введите число: ')
while not is_digital_valid(amount_passwords):
    print('Введите цифру!')
    amount_passwords = input()
else:
    amount_passwords = int(amount_passwords)

size_password = input('Какой длинный должен быть пароль? Введите число: ')
while not is_digital_valid(size_password):
    print('Введите цифру!')
    size_password = input()
else:
    size_password = int(size_password)

numbers = input('Должны ли быть цифры в пароле? ')
letters_upper = input('Должны ли быть символы верхнего регистра в пароле? ')
letters_lower = input('Должны ли быть символы нижнего регистра в пароле? ')
symbols = input('Должны ли быть символы? ')
speciol_symbols = input('Должны ли быть неоднозначные символы? ')

list_answer = [numbers, letters_upper, letters_lower, symbols, speciol_symbols]

char_list = generate_chars(list_answer)

passwords = []
for i in range(amount_passwords):
    password = generate_password(size_password, char_list)
    passwords.append(''.join(password))

print(f'Длина паролей: {size_password}. Количество паролей: {amount_passwords}.')
print(passwords)