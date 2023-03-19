num = int(input())

ten = num // 10
one = num % 10

new = -1
cycle = 0

if num < 10:
  ten = 0

if cycle == 0:
  new_one = (ten + one) % 10
  new = one * 10 + new_one
  cycle += 1
  
while new != num:
  cycle += 1
  ten = new // 10
  one = new % 10
  new_one = (ten + one) % 10 
  new = one * 10 + new_one

print(cycle)