import math

answer_cipher = input('Шифрование или дешефрование? Напишите "ш" или "д": ').lower()
language = input('Русский или английский язык? Напишите "р" или "а": ').lower()
step_move = int(input('Шаг сдвига? Напишите цифру: '))

upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

phrase = input()
phrase_new = ''

# шифрование
if answer_cipher == 'ш':
    if language == 'р':
        for i in phrase:
            if i in lower_rus_alphabet:
                phrase_new += lower_rus_alphabet[(lower_rus_alphabet.index(i) + step_move)
                                                 % len(lower_rus_alphabet)]
            elif i in upper_rus_alphabet:
                phrase_new += upper_rus_alphabet[(upper_rus_alphabet.index(i) + step_move)
                                                 % len(upper_rus_alphabet)]
            else:
                phrase_new += i
    elif language == 'а':
        for i in phrase:
            if i in lower_eng_alphabet:
                phrase_new += lower_eng_alphabet[(lower_eng_alphabet.index(i) + step_move)
                                                 % len(lower_eng_alphabet)]
            elif i in upper_eng_alphabet:
                phrase_new += upper_eng_alphabet[(upper_eng_alphabet.index(i) + step_move)
                                                 % len(upper_eng_alphabet)]
            else:
                phrase_new += i

# дешифровка
elif answer_cipher == 'д':
    if language == 'р':
        for i in phrase:
            if i in lower_rus_alphabet:
                phrase_new += lower_rus_alphabet[(lower_rus_alphabet.index(i) - step_move)
                                                 % len(lower_rus_alphabet)]
            elif i in upper_rus_alphabet:
                phrase_new += upper_rus_alphabet[(upper_rus_alphabet.index(i) - step_move)
                                                 % len(upper_rus_alphabet)]
            else:
                phrase_new += i
    elif language == 'а':
        for i in phrase:
            if i in lower_eng_alphabet:
                phrase_new += lower_eng_alphabet[(lower_eng_alphabet.index(i) - step_move)
                                                 % len(lower_eng_alphabet)]
            elif i in upper_eng_alphabet:
                phrase_new += upper_eng_alphabet[(upper_eng_alphabet.index(i) - step_move)
                                                 % len(upper_eng_alphabet)]
            else:
                phrase_new += i

# когда цикл вместо сдвига
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
