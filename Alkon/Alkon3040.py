space = []
flag = 0

for _ in range(9):
  space.append(int(input()))


for i in range(8):
  if flag:
    break
  for j in range(i+1, 9):
    if sum(space) - space[i] - space[j] == 100:
      space.pop(j)
      space.pop(i)
      flag = 1
      break

for s in space:
  print(s)
