num, jack = map(int, input().split())

nums = list(map(int,input().split()))

sum = 0

for i in range(num):
  for j in range(i+1,num):
    for k in range(j+1,num):
      temp = nums[i] + nums[j] + nums[k]
      if temp > jack:
        continue
      else:
        sum = max(sum, temp)

print(sum)
  