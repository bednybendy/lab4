y=int(input())
if (y%4==0 and y%100!=0) or y%400==0: print (f'год {y} високосный')
else: print(f'год {y} не високосный ')