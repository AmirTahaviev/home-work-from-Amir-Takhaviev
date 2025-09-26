f = open('text.rtf', 'r')
lines = f.readlines()
print(lines)
numbers = list(map(int, lines[0].split()))
sign = lines[1].strip()

if sign == '+':
    x = sum(numbers)
elif operation == '-':
    x = numbers[0] - sum(numbers[1:])
elif operation == '*':
    x = 1
    for num in numbers:
        x *= num

with open('text.rtf', 'w') as file:
    file.write(str(x))

f.close()