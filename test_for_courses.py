number = int(input())
number_list = []
count = 0
for i in range(number):
    a = int(input())
    number_list.append(a)
number_sum = int(input())
for i in range(number - 1):
    if number_list[i] * number_list[i + 1] == number_sum:
        count += 1
    for j in range(i - 1):
        if number_list[j] * number_list[j + 1] == number_sum:
            count += 1
if count > 0:
    print('ДА')
else:
    print('НЕТ')
