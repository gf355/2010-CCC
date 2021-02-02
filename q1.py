number = int(input(''))
count = 0
for i in range(0, 6):
    for j in range(i, 6):
        if i + j == number:
            count += 1
print(count)
