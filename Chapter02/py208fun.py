# -*- coding: utf-8 -*-

def f01(a,b,c):
	print('a,b,c,',a,b,c)
	a2,b2,c2,=a+c,b*2,c*2
	return a2,b2,c2
    
#1
print('\n#1')
x,y,z=f01(1,2,3)
print('x,y,z,',x,y,z)

#2
print('\n#2')
x,y,z=f01(x,y,z)
print('x,y,z,',x,y,z)

