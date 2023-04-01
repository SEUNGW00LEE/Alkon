

def hanoi_tower(N, start, end):
  if N == 1:
    print(start, end)
    return
  hanoi_tower(N-1, start, 6-start-end)
  print(start, end)
  hanoi_tower(N-1, 6-start-end,end)

N = int(input())
  
print(2**N-1)
if N <= 20:
  hanoi_tower(N,1,3)