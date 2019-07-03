from itertools import combinations
m,a=map(int,input().split())
p=len(str(m))
l=list(combinations(str(m),p-a))
l=(sorted(l))
y="".join(l[0])
print(y)
