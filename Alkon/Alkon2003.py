number, jack = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

left, right = 0, 1

while right <= number and left<= right:
  temp = nums[left:right]
  total = sum(temp)
  
  if total == jack:
    count += 1
    right += 1
  elif total > jack:
    left += 1
  else :
    right += 1    

print(count)
