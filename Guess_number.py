right = int(input())
count = 0
while right != 1:
    if right % 2 != 0:
        right += 1
    right = right // 2
    count += 1
print(count)