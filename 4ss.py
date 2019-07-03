sou,jit1=map(str,input().split())
sat=0
if len(sou)>len(jit1):
  sou,jit1=jit1,sou
i=0
while i<len(sou):
  sat+=(ord(jit1[i])-ord(sou[i]))
  i+=1
for i in range(i,len(jit1)):
  sat+=ord(jit1[i])-ord('a')+1
print(sat)
