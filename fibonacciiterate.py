#printing fibonacci series
n1=0
n2=1
cnt=0
n=int(input("enter the number: "))
while (cnt<=n):
	print(n1)
	nth=n1+n2
	n1=n2
	n2=nth
	cnt+=1

