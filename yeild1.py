def sq(l,u):
    for i in range(l,u+1):
        yield i**3

def val():
    l=int(input('Enter the Lower Limit::'))
    u=int(input('Enter the Upper Limit::'))
    sq(l,u)
    show(l,u)

def show(l,u):
    print('Cube from ',l,' to ',u)
    for cube in sq(l,u):
        print(l,':',cube)
        l+=1
val()
