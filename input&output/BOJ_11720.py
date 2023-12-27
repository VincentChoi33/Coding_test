def split(word):
    return [char for char in word]
n=input()
x=input()
list=split(x)
k=0
for i,l in enumerate(list):
    k+=int(l)
print(k)
