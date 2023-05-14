
def Find_factors(n):
  # run a loop from 1 to n --  brute force
  for i in range(1,n+1):
    if(n%i==0):
      print(i,end=" ")


n=int(input())
Find_factors(n)