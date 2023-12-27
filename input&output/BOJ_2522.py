x = int(input())

for i in range(1,x+1):
    y=' '*(x-i) + '*'*i
    print(y)

for i in range(1,x):
    y=' '*(i) + '*'*(x-i)
    print(y)
