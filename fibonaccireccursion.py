def fibo(n):
	if n==0:
		return 0
	elif n==1 or n==2:
		return 1;
	else:
		return(fibo(n-1)+fibo(n-2))
number=int(input("enter a number: "))
for i in range(number):
	print(fibo(i))	
