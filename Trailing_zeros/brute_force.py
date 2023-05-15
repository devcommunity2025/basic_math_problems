
import math

def trailzeros(n):
  '''
  trailing zeros means the last repeated zeros
  eg: 5! =120  which has 1 zero at the end
   12! = 47,90,01,600 has 2 zeros
  '''

  #first let us find the factorial of n
  fact=math.factorial(n)
  
  #divide fact by 10 until it becomes not divisble
  count=0
  while(fact%10==0):
    count+=1
    fact=fact//10
  return count


n=int(input())
zeros=trailzeros(n)
print(zeros)