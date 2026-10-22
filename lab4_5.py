a,b=float(input('')),float(input(''))
op=input('')
match op:
    case '+': print(f'результат {a+b}')
    case '-': print(f'результат {a-b}')
    case '*': print(f'результат {a*b}')
    case '/': 
        if b!=0: print(f'результат {a/b:.2f}')
        else:print('я не умею делить на ноль(')
    case '_': print('не знаю таких операций')