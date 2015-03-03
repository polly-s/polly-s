import sys

while 1:
  a=input()
  if a==0:
	exit()
  b=raw_input()
  c=len(b)
  i=0
  t=1
  j=1
  s=1
  while i<a:
        k=i
        while k<c:
                 sys.stdout.write(b[k])
                 if j==1:
                        k=k+2*a-t
                 else:
                      k=k+s
                 j=j*(-1)
        t=t+2
        s=s+2
        i=i+1
        j=1
  print

