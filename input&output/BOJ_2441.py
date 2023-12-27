x = int(input())
for i in range(x):
    y=''
    for j in range(x):
        if j>=i:
            y+='*'
        else:
            y+=' '
    print(y)
