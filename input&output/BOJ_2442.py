x = int(input())

for i in range(1,x+1):
    y = ' '* (x-i) + '*'*(2*i-1)
    print(y)
