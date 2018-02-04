n=int(raw_input())
fact=1
while(n>0):
  for i in range(1,n+1):
	  fact=fact*i
	  n=n-1
  print fact
