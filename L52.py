n=int(input("What is your number?"))

def perfectList(n):
    total=0
    if (n != 0):
        for x in range (1,n):
            if n%x==0:
                total=total+x
        if total==n:
            print(n)
            n=n-1
        else:
            n=n-1
    perfectList(n)

perfectList(n)

