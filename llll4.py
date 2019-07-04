a=int(input())
sum=0
t=a
while a>0:
	x=a%10
	sum=sum+x*x*x
	a=a//10
if t==sum:
	print("yes")
else:
	print("no")
