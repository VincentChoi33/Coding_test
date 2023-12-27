import math
def split(word):
    return [char for char in word]
x=input()
list=split(x)
for i in range(math.ceil(len(list)/10)):
    q=''
    for j in range(10):
        try:
            q+=(list[i*10+j])
        except:
            break
    print(q)
