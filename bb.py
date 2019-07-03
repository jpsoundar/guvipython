m=int(input())
if (m>1):   
   for i in range(2, m//2):   
       if (m %i) == 0: 
           print("no")
           break
   else: 
       print("yes") 
else: 
   print("no")
