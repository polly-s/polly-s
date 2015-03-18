from numpy import *

C=np.arange(4)

C+=1

C=C[::-1]

C=C.reshape(2,2)

np.tile(C,[2,3])


