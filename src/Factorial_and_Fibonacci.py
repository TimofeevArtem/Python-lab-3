def factorial(n: int):
    """Функция считает факториал числа"""
    a = [0] * 1001
    for i in range(n + 1):
        if i == 0:
            a[i] = 1
        elif i == 1:
            a[i] =  1
        else:
            a[i] = a[i - 1] * (i)
    return a[n]

def factorial_recursive(n: int):
    """Функция рекурсивно считает факториал числа"""
    if n < 0:
        print("incorrect input")
        return -1
    if n == 0:
        return 1
    else:
        return factorial_recursive(n - 1) * n

def fibo(n: int):
    """Функция считает число фибоначчи под введенным номером"""
    a = [0] * (10**4 + 1)
    for i in range(n + 1):
        if i == 0:
            a[i] = 0
        elif i == 1:
            a[i] = 1
        elif i == 2:
            a[i] = 1
        else:
            a[i] = a[i - 1] + a[i - 2]
    return a[n - 1]
        
def fibo_recursive(n: int):
    """Функция рекурсивно считает число фибоначчи под введенным номером"""
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)