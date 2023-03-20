import sys
input = sys.stdin.readline

t = int(input())
coor = []

for _ in range(t):
  [x, y] = map(int, input().split())
  coor.append([x,y])
  
coor = sorted(coor)

for i in range(t):
  print(coor[i][0], coor[i][1])