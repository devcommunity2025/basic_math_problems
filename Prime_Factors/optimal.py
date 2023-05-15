
import math
def prime_factor(n):
  
  if(n<=1):
    return 
  '''
  instead of running loop n times we can go for sqrt(n) times
  '''
  s=int(math.sqrt(n))
  for i in range(2,s+1):
    while(n%i==0):
      print(i,end=" ")
      n=n//i
      
  '''
  we run until sqrt(n) so if n is prime it will not enter for loop and prints nothing
  So to avoid the problem with prime input we can say if n>1 print n
  '''
  if(n>1):
    print(n)


n=int(input())
prime_factor(n)