from math import *
a,b,c=float(input()),float(input()),float(input())
if a==0: print('')
else:
    d=b**2-4*(a*c)
    if d>0: print(f'два корня x1={(-d+sqrt(d))/(2*a)} x2= {(-d-sqrt(d))/(2*a)}')
    elif d==0: print(f'один корень x={-b/(a*2)}')
    else: print('нет корней')