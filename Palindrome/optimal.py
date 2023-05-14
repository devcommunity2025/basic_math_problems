
def check_palin(n):
  s=0
  temp=n
  if(n<0):
    return False
  while(temp>0):
    rem=temp%10
    s=s*10+rem
    temp=temp//10
  return (s==n)

n=int(input())
palin=check_palin(n)
print(palin)