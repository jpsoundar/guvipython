from itertools import combinations
gsd,n2d=input().split()
n2d=int(n2d)
l=[]
dd=combinations(gsd,len(gsd)-n2d)
for i in list(dd):
  l.append("".join(i))
print(min(l))
