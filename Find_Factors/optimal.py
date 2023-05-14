import math

def Find_factors(n):
  # factors exists <= sqrt(n) 
  '''
  example: 12 factors- 1 x 12  sqrt(n)= 3  type cast to int
                       2 x 6
                       3 x 4
  '''
  
  s=int(math.sqrt(n)) 
  for i in range(1,s+1): # prints 1 2 3
    if(n%i==0):
      print(i,end=" ")
  for i in range(s,0,-1):
      if(n%i==0 and (n//i)!=i):
        print(n//i,end=" ") # if 3 divides 12 then prints 12/3 =4
  


n=int(input())
Find_factors(n)