
upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!,.""-'

phrase = input().split(' ')
phrase_new = ''
phrase_copy = phrase[:]


for i in range(len(phrase_copy)):
    for j in phrase_copy[i]:
        if j in punctuation:
            phrase_copy[i] = phrase_copy[i].replace(j, '')

for i in range(len(phrase)):
    for j in phrase[i]:
        if j in lower_eng_alphabet:
            phrase_new += lower_eng_alphabet[(lower_eng_alphabet.index(j) + len(phrase_copy[i])) % len(lower_eng_alphabet)]
        elif j in upper_eng_alphabet:
            phrase_new += upper_eng_alphabet[(upper_eng_alphabet.index(j) + len(phrase_copy[i])) % len(upper_eng_alphabet)]
        else:
            phrase_new += j
    phrase_new += ' '

print(phrase_new)

