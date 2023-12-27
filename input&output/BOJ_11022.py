n = int(input())
for i in range(n):
    x= input()
    A=int(x.split(' ')[0])
    B=int(x.split(' ')[1])    
    print('Case #'+str(i+1)+': '+str(A)+' + '+str(B)+' =',A+B)
