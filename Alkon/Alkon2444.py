count  = int(input())

s = count 

for i in range(1,count+1):
  print(" " * (count-i) + "*" * (i * 2 - 1))
  i += 1

for t in range(1,count):
  print(" " * t + "*" * (s * 2 - 3))
  s -= 1


# " " * (n-1) + * * (1)
# " " * (n-2) + * * (3)
# " " * (n-3) + * * (5)
# ...
# " " * (n-i) + * * i
# " " * (n-i) + * * i

# 2n - 1
# 
#