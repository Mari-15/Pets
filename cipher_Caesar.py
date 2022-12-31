import math


def un_cript(phrase_func, language_lower, language_upper, step):
    phrase_new_func = ''
    for j in phrase_func:
        if j in language_lower:
            phrase_new_func += language_lower[(language_lower.index(j) + step) % len(language_lower)]
        elif j in language_upper:
            phrase_new_func += language_upper[(language_upper.index(j) + step) % len(language_upper)]
        else:
            phrase_new_func += j
    return phrase_new_func


def in_cript(phrase_func, language_lower, language_upper, step):
    phrase_new_func = ''
    for j in phrase_func:
        if j in language_lower:
            phrase_new_func += language_lower[(language_lower.index(j) - step) % len(language_lower)]
        elif j in language_upper:
            phrase_new_func += language_upper[(language_upper.index(j) - step) % len(language_upper)]
        else:
            phrase_new_func += j
    return phrase_new_func


def is_valid_digit_answer(num):
    if num.isdigit():
        return True
    else:
        return False


def is_valid_abc_answer(abc):
    if abc == 'д' or abc == 'н':
        return True
    else:
        return False


step_cycle = input('Сдвиг циклом?\nВведите "д" или "н": ').lower()
while not is_valid_abc_answer(step_cycle):
    step_cycle = input('Ответ может быть только "д" или "н".\nВведите ответ: ').lower()

print()
step_move = input('Шаг сдвига?\nНапишите цифру: ')
while not is_valid_digit_answer(step_move):
    step_move = input('Шагом сдвига может быть только цифра.\nВведите цифру: ')
step_move = int(step_move)

print()
answer_cipher = input('Шифрование или дешефрование? \n'
                      'Напишите "д" для шифрования или "н" для дешефривания: ').lower()
while not is_valid_abc_answer(answer_cipher):
    answer_cipher = input('Ответ может быть только "д" или "н".\nВведите ответ: ').lower()

print()
language = input('Русский или английский язык? \n'
                 'Напишите "д" для русского или "н" для английского: ').lower()
while not is_valid_abc_answer(language):
    language = input('Ответ может быть только "д" или "н".\nВведите ответ: ').lower()

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

print()
phrase = input()

# шифрование
if step_cycle == 'н':
    if answer_cipher == 'д':
        if language == 'д':
            phrase_new = un_cript(phrase, lower_rus_alphabet, upper_rus_alphabet, step_move)
        elif language == 'н':
            phrase_new = un_cript(phrase, lower_eng_alphabet, upper_eng_alphabet, step_move)

# дешифровка
    elif answer_cipher == 'н':
        if language == 'д':
            phrase_new = in_cript(phrase, lower_rus_alphabet, upper_rus_alphabet, step_move)
        elif language == 'н':
            phrase_new = in_cript(phrase, lower_eng_alphabet, upper_eng_alphabet, step_move)
    print(phrase_new)

# когда цикл вместо сдвига
if step_cycle == 'д':
    if answer_cipher == 'д':
        for j in range(step_move):
            if language == 'а':
                for i in phrase:
                    if i in lower_eng_alphabet:
                        phrase_new += lower_eng_alphabet[(lower_eng_alphabet.index(i) - j)
                                                         % len(lower_eng_alphabet)]
                    elif i in upper_eng_alphabet:
                        phrase_new += upper_eng_alphabet[(upper_eng_alphabet.index(i) - j)
                                                         % len(upper_eng_alphabet)]
                    else:
                        phrase_new += i
        print(*phrase_new.split('.'), sep='\n')
