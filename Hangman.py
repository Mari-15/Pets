import random


def get_word(word_l):
    word_index = random.randint(0,9)
    word = word_l[word_index]
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_comp = word
    word_completion = '_' * len(word_comp)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print(f'В слове {len(word_comp)} букв.')
    while tries > 0:
        player_suggestion = str(input('Введите букву или слово: '))
        if len(player_suggestion) == 1:
            if player_suggestion not in alfabet_upper and player_suggestion not in alfabet_lower:
                print('Необходимо ввести букву русского алфавита или слово.')
            elif player_suggestion.upper() in guessed_letters:
                print('Вы уже вводили эту букву.')
            elif player_suggestion.upper() in word_comp:
                for i in range(len(word_comp)):
                    if word_comp[i] == player_suggestion.upper():
                        if i == 0:
                            word_completion = player_suggestion.lower() + word_completion[1:]
                        elif i != 0:
                            word_completion = word_completion[:i] + \
                                          player_suggestion.lower() + word_completion[i+1:]
                        guessed_letters.append(player_suggestion.upper())
                if word_completion.upper() == word_comp:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    if tries == 6:
                        print('Поздравляем, вас не повесили совсем!')
                    else:
                        print(display_hangman(tries))
                    break
                else:
                    print(word_completion)
            elif player_suggestion.upper() not in word_comp:
                print('К сожалению такой буквы нет в слове.')
                tries -= 1
                guessed_letters.append(player_suggestion.upper())
        elif player_suggestion.lower() in guessed_words:
            print('Вы уже вводили это слово.')
        elif player_suggestion.upper() == word_comp:
            print('Поздравляем, вы угадали слово! Вы победили!')
            if tries == 6:
                print('Поздравляем, вас не повесили совсем!')
            else:
                print(display_hangman(tries))
            break
        elif player_suggestion.upper() != word_comp:
            guessed_words.append(player_suggestion.lower())
            tries -= 1
            print('Вы не угадали слово.')
    else:
        print()
        print('К сожалению вы не угадали слово.')
        print(display_hangman(tries))


word_list = ['банан', 'огурец', 'помидор', 'волос', 'яблоко',
             'персик', 'арбуз', 'совет', 'синоним', 'деньги']

alfabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

word_for_game = get_word(word_list)
play(word_for_game)

print()
play_again = input('Если хотите сыграть еще, введите "да": ')
print()
while play_again.lower() == 'да':
    if play_again.lower() == 'да':
        word_for_game = get_word(word_list)
        play(word_for_game)
        play_again = input('Если хотите сыграть еще, введите "да": ')
else:
    print('Спасибо за игру! Приходите еще.')
