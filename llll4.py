a=int(input())
sum=0
t=a
while a>0:
	x=s%10
	sum=sum+x*x*x
	a=a//10
if t==sum:
	print("yes")
else:
	print("no")
