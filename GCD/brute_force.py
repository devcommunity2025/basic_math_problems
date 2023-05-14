
def Find_gcd(n1,n2):
  #naive approach or brute force
  mini=min(n1,n2) 
  #run a loop from 1 to min(n1,n2)
  gcd=0
  for i in range(1,mini+1):
    if(n1%i==0 and n2%i==0):
      gcd=i
  return gcd

a,b=input().split()
gcd=Find_gcd(int(a),int(b))
print(gcd)
