f = open('in.txt', 'r')
in_file = f.readlines()
f.close()
A= [int(i) for i in in_file[1].strip().split(' ')]
B= []
for j in range (3,len(in_file)):
    B.append([int(i) for i in in_file[j].split(' ')])

#@profile
def func(a,x,y):
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

for task in B:
    print func(task[0],task[1],task[2])

print A
