N=input()
A= []
j=0
for i in range(N):
    A.append(input()) 
M=input()
def func(a,x,y,A):
   if a==0:
      A[x]=y
      return(A)
   else:
      max=A[x]
      k=max
      while 1:
           x=x+1
           if x>y:
               break
           k=k+A[x]
           if max<k:
                 max=k
      return(max)
while 1: 
    if j==M:
       exit()
    a=input()
    x=input()
    y=input()
    print(func(a,x,y,A))
    j=j+1
