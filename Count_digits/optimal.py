
def Count_digits(n):
  cnt=0
  while(n>0):
    # removing last digit at every iteration and incrementing cnt
    n=n//10
    cnt+=1
  return cnt


n=int(input())
digits=Count_digits(n)
print(digits)