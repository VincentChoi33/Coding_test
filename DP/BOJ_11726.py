n = int(input())

list = [0,1,2]

for i in range(3,n+1):
  list.append(list[i-1]+list[i-2])
if n ==1:
  print(n)
else:
  print(list[-1]%10007)
