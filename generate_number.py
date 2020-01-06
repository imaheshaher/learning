k=0
f=0 
n=0
c=0
while k<100:
	n=a=n
	while a>0:
		d=a%10
		a=int(a/10)
		if d==3 or d==7:
			f=1
		else:
			f=0
			break
	if f==1:
		print(k,n)
		k+=1
	n+=1
	