import sys

while 1:

   a=input()
   b=input()
   c=input()
   if (a==0)and(b==0)and(c==0):
	   exit()
   if b-a==c-b :
      sys.stdout.write('AP')
      sys.stdout.write(' ')
      print(c+b-a)
   else :
      sys.stdout.write('GP')
      sys.stdout.write(' ')
      print(c*b/a)
   print
