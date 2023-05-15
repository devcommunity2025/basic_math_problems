
def isprime(n):
  if(n<=1):
    return "Not Prime"
  # run a loop from 2 to (n-1) if any number divides n then n is not Prime
  for i in range(2,n):
    if(n%i==0):
      return "Not Prime"
  return "Prime"


n=int(input())
result=isprime(n)
print(result)