while True:
    try:
        x = input()        
        A=int(x.split(' ')[0])
        B=int(x.split(' ')[1])
        print(A+B)
    except:
        break
