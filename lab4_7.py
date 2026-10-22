a,b,c=float(input()),float(input()),float(input())
if a+b>c and a+c>b and b+c>a:
    if a==b==c: print('равносторонний треугольник')
    elif a==b or a==c or b==c: print('равнобедренный треугольник')
    else: print('разносторонний треугольник')
else: print('некорректные данные')