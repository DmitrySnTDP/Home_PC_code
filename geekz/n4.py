for n in range(1000,10000):
    a = ((n//1000))+((n//100%10))
    b = ((n//10%10))+((n%10))

    if b<a:
        ab=str(a)+str(b)
        if int(ab)==1510:
            print(n)
            break
    else:
        ba=str(b)+str(a)
        if int(ba)==1510:
            print(n)
            break