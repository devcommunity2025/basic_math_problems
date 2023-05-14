
def Find_lcm(n1,n2):
  maxi=max(n1,n2)
  k=n1*n2
  for i in range(maxi,k+1):
    if(i%n1==0 and i%n2==0):
      return i



a,b=input().split()
lcm=Find_lcm(int(a),int(b))
print(lcm)
