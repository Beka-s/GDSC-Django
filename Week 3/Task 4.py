sum = 0
count_three = 0
count_five = 0

for i in range(1,51):
    if i % 2 == 0:
        if i == 50:
            print(f'Five =', end=" ")
            count_five += 1
        elif i == 30:
            print(f'Three and Five +', end=" ")
            count_three += 1
            count_five += 1
        elif i % 3 == 0:
            print(f'Three +', end=" ")
            count_three += 1
        elif i % 5 == 0:
            print(f'Five +', end=" ")
            count_five += 1
        else:
            print(f'{i} +', end=" ")
        sum = sum + i
print(sum)
print(f"Amount of number replaced by 'three': {count_three}")
print(f"Amount of number replaced by 'five': {count_five}")