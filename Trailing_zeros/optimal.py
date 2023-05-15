
import math

def trailzeros(n):
  '''
  instead of finding factorial and then counting zeros, we can have optimal approach
  
  eg: n= 12 has 2 zeros...we get zeros when there is combination of 2 and 5
  no. of 2's are more than 5..so simply if we count no. of 5,25,125,625,..<=n
  this count gives no. of zeros
  
  eg: 125= 1*2*..5*..25*26..*125 count no. of 5,25 and 125
  '''
  count=0
  i=5
  while(i<=n):
    count=count+ n//i
    i=i*5
  return count

n=int(input())
zeros=trailzeros(n)
print(zeros)