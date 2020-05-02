l=[]#append binary digit
def decimal_binary(num):
    while num>0:
        mod=num%2
        l.append(mod)
        num=int(num//2)
    printfun()
def binary_decimal(num):
    dec=0
    n=0
    while num>0:
        mod=num%10
        if mod==1:
            dec=2**n+dec
        num=int(num//10)
        n+=1

    print(dec)

def printfun():
    for i in range(len(l)-1,-1,-1):
        print(l[i],end="")
    print()


#enter number to print decimal digit into binary
dec_to_binary=int(input("enter number to print decimal digit into binary:: "))
decimal_binary(dec_to_binary)

#enter number to print binary digit into decimal ex.1100
binary_to_dec=int(input("enter number to print binary digit into decimal ex.1100:: "))
binary_decimal(binary_to_dec)

