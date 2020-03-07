a=[1,9,4,7]  #First array
b=[2,1,4,8,7,9,6,5] #second array


c=0
for i in a:
	for j in b:
		
		if i==j:
			c+=1
			break
		
if c==len(a):
	print('Yes, It is the subset of SET')
else:
	print('No, It is not subset...')
