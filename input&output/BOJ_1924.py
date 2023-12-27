x=input()
m=int(x.split(' ')[0])
d=int(x.split(' ')[1])
a=31
b=28
c=30
day=0
if m == 1:
    day =0
if m == 2:
    day =a
if m == 3:
    day =a+b
if m == 4:
    day =a+b+a
if m == 5:
    day =a+b+a+c
if m == 6:
    day =a+b+a+c+a
if m == 7:
    day =a+b+a+c+a+c
if m == 8:
    day =a+b+a+c+a+c+a
if m == 9:
    day =a+b+a+c+a+c+a+a
if m == 10:
    day =a+b+a+c+a+c+a+a+c
if m == 11:
    day =a+b+a+c+a+c+a+a+c+a
if m == 12:
    day =a+b+a+c+a+c+a+a+c+a+c
    
date = day+d
if date%7 ==1:
    print('MON')
if date%7 ==2:
    print('TUE')
if date%7 ==3:
    print('WED')
if date%7 ==4:
    print('THU')
if date%7 ==5:
    print('FRI')
if date%7 ==6:
    print('SAT')
if date%7 ==0:
    print('SUN')    
