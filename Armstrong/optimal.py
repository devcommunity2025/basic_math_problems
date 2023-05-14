
def isArmstrong(n):
  temp=n
  s=0
  while(temp>0):
    rem=temp%10
    s=s+pow(rem,3)
    temp=temp//10
  return (s==n)
  

n=int(input())
ans=isArmstrong(n)
print(ans)