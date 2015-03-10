for m in range(10):
 N=input()
 A=[]
 for i in range(N):
     A.append(raw_input()) 
 M=input()
 j=0
 d=0
 k=0
 def func(x):   
       if x==0:
               d=0
               for j in range(N):
                      if A[j]=="(":
                            d=d+1
                      else:
                            d=d-1
                            if d<0:
                                 print('NO')
                                 exit()
               if d>0:
                     print('NO') 
               else:
                     print('YES')      
       else:
          if A[x]=="(":
               A[x]=")"
          else:
               A[x]="("
          print(A)
 for k in range(M):
            x=input()
            func(x)
