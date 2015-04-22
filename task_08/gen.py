#!/usr/bin/python

A="400\n"
for i in xrange(400):
    A+=str(i)+' '

A+='\n'
A+='1000\n'
for i in xrange(1000):
    A+='1 0 300\n'

f = open('in.txt', 'w')
f.write(A)
f.close()
