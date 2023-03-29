t = int(input())

for _ in range(t):
  ox = input()
  li = list(ox)
  sum = 0
  flag = 1
  for i in li:
    if i == 'O':
       sum += flag
       flag += 1
    else:
      flag = 1
      
  print(sum)
  
