x = int(input())

for i in range(1,x):
    y='*'*i + ' '*(2*(x-i)) + '*'*i
    print(y)

print('*'*2*x)

for i in range(x-1,0,-1):
    y='*'*i + ' '*(2*(x-i)) + '*'*i
    print(y)


