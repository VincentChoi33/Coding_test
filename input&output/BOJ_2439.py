x = int(input())

for k in range(x):
    i=x-k-1
    y=''
    for j in range(x):
        if i<=j:
            y+='*'
        else:
            y+=' '
    print(y)

