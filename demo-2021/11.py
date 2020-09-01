from math import ceil

i=3 #т.к. 3 бита требуется для кодирования 8 симоволов (2**3=8)
k=15
I=ceil(i*k/8)
iOneObject=I+24 #байт на один объект
iObjects = iOneObject*20
print(iObjects)
