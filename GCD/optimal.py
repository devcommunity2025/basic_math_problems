
def Find_gcd(n1,n2):
  # First find gcd using euclid's algorithm
  gcd=0
  while(n1!=0 and n2!=0):
    if(n1>n2):
      n1=n1%n2
    else:
      n2=n2%n1
  if(n1==0):
    gcd=n2
  else:
    gcd=n1
  return gcd    



a,b=input().split()
gcd=Find_gcd(int(a),int(b))
print(gcd)
