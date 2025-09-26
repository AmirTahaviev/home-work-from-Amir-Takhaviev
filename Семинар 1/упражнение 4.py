f = open('text.txt', 'r+')
lines = f.readlines()

numbers = list(map(int, lines[0].split()))
sign = lines[1].strip()

if sign == '+':
    x = sum(numbers)
elif sign == '-':
    x = numbers[0] - sum(numbers[1:])
elif sign == '*':
    x = 1
    for num in numbers:
        x *= num

with open('text.txt', 'w') as file:
    file.write(str(x))

f.close()