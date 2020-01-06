#generate numbers using given two numbers
print('generate numbers using given two numbers
')
x=int(input('enter the first number'))
y=int(input('enter the second number'))

k=0
f=0 
n=0

while k<100:
	n=a=n
	while a>0:
		d=a%10
		a=int(a/10)
		if d==x or d==y:
			f=1
		else:
			f=0
			break
	if f==1:
		print(k,n)
		k+=1
	n+=1
	
