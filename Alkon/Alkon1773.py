number, time = map(int, input().split())
space = [0] * (time+1)

for i in range(number) :
  num = int(input())
  if num == 1: #시간초과로 추가
    print(time)
    quit()
  for s in range(num, time+1, num):
    space[s] = 1

print(sum(space))