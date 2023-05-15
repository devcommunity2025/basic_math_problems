
def prime_factor(n):
  
  if(n<=1):
    return # as below 1 we can't have prime factors
 
  '''eg 12-> 2*2*3 divide the number until it can't be divisible by 2
     we get 2 two times printed next we divide with 3...the process repeats
  '''
  for i in range(2,n+1):
    while(n%i==0):
      print(i,end=" ")
      n=n//i

n=int(input())
prime_factor(n)