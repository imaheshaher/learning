#Given a Number N write a code to print all positibe numbers less than N in which all adjecent digits differ by 1


'''Example ::
    If Number is 14 the output will be ::
        0,1,2,3,4,5,6,7,8,9,10,11'''


num = int(input('Enter The Number::'))
for i in range(num):
    f=0 #flag =0
    l=[] #list
    n=i
    while n>0: #seperate Number digit
        d=n%10
        n=int(n/10)
        l.append(d) #append number here
    if i>=0:
        if i<10:
            print(i)
        for j in range (len(l)-1): 
            
            f=0
            if l[j]-l[j+1] == -1 or l[j]-l[j+1] == 1: #check the adjecent number is differ by 1 or not
                f=1
            else:
                f=0
                break

    if f==1:
        print(i)



     
        
