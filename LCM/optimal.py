
def Find_lcm(n1,n2):
  # lcm*gcd = n1*n2
  # First find gcd using euclid's algorithm
  k=n1*n2
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
  #finding lcm here k=n1*n2
  lcm=k//gcd
  return lcm    



a,b=input().split()
lcm=Find_lcm(int(a),int(b))
print(lcm)
