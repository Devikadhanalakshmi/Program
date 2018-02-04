a=int(raw_input())
b=int(raw_input())
for i in range(a,b+1):
  sum=0
  temp=i
  while(temp>0):
   n=temp%10
   sum=sum+n*n*n
   temp=temp/10
  if i==sum:
    print (i)
   
  
  
