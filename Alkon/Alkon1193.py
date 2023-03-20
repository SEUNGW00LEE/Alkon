num = int(input())

line = 1
num1 = 0
num2 = 0
 
while num > line:
  num -= line
  line += 1

if line % 2 == 0:
  num1 = num
  num2 = line - num + 1

if line % 2 == 1:
  num1 = line - num + 1
  num2 = num

print(f'{num1}/{num2}')