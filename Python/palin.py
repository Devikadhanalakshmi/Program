rev=0
n=int(raw_input())
t=n
while(n!=0):
	r=n%10
	rev=rev*10+r
	n=n/10
	if(t==rev):
		print yes
	else:
    print no
