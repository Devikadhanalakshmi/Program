#include <stdio.h>
 
int main()
{
   int a,b,i;
   scanf("%d",&a);
   scanf("%d",&b);
   for(i=a+1;i<=b;i++)
   {
   	n=0;
   	for(j=2;j<i;j++)
   	{
             if(i%j==0)
             {
               n=1
             }
   	}
   	if(n==0)
   	{
   	printf("%d",i)
   }
 
   }
   return 0;
}
