sum=0
n=int(raw_input())
n=temp
while(n>0):
  n=n%10
  sum=sum+n**3
  n=n/10
if(sum==temp):
   print yes
else:
   print no
