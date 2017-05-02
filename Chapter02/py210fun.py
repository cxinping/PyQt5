# -*- coding: utf-8 -*-
 
import functools

def add(a, b):
    return a + b

#1
print('\n#1')
rst1 = add(4, 2)
print('add(4, 2)=' , rst1)

plus3 = functools.partial(add, 3)
plus5 = functools.partial(add, 5)

#2
print('\n#2')
rst2 = plus3(4)
print('plus3(4)=' , rst2)

rst3 = plus3(7)
print('plus3(7)=' , rst3)

rst4 = plus5(10)
print('plus5(10)=' , rst4)



