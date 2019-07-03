nua,nub=input().split()
S=abs(len(nua)-len(nub))
for v in range(len(nua)):
    if len(nub)==1 and nub[v] in nua:
        break
    if nua[v]!=nub[v]:
        S+=1
print(S)
