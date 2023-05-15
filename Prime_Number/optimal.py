
import math

def isprime(n):
  if(n<=1):
    return "Not Prime"
    
  '''instead running a loop nearly n times
     we know we can get factors by running loop sqrt(n) times
     if any number divides n we return not prime else prime
  '''
  
  s=int(math.sqrt(n))
  for i in range(2,s+1):
    if(n%i==0):
      return "Not prime"
  return "Prime"


n=int(input())
result=isprime(n)
print(result)