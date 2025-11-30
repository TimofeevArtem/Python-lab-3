from Factorial_and_Fibonacci import *
from Sorting import *
from Stack import *

def stack_processing(stack):
    """Функция обработки стека"""
    while True:
        user_input_stack = input("Введите команду для стека (pop, push, peek, min, len, is_empty, back): ").strip().lower()
        
        if user_input_stack == "back":
            break
        
        elif user_input_stack in ["pop", "pop()"]:
            try:
                return_num = stack.pop()
                print(f"Удаленный элемент: {return_num}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_stack in ["push", "push()"]:
            user_input_num = input("Введите элемент, который хотите добавить: ").strip()
            if user_input_num.lower() == "back":
                continue
            try:
                num = int(user_input_num)
                stack.push(num)
                print(f"Добавленый элемент: {num}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_stack in ["peek", "peek()"]:
            try:
                return_num = stack.peek()
                print(f"Верхний элемент: {return_num}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_stack in ["min", "min()"]:
            try:
                return_num = stack.min()
                print(f"Минимальный элемент: {return_num}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_stack in ["len", "len()"]:
            try:
                return_num = len(stack)
                print(f"Длина стека: {return_num}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_stack in ["is_empty", "is_empty()"]:
            try:
                return_ans = stack.is_empty()
                if return_ans == True:
                    print("Стек пуст\n")
                elif return_ans == False:
                    print("Стек не пуст\n")
                else:
                    print("Неверный ввод\n")
            except:
                print("Неверный ввод\n")
        
        else:
            print("Неверная команда. Доступные команды: pop, push, peek, min, len, is_empty, back\n")

def sorting_processing():
    """Функция обработки сортировок"""
    while True:
        print("Доступные методы сортировки: quick, bubble, count, radix, bucket и heap")
        user_input_sort = input("Введите название метода сортировки (или back для выхода): ").strip().lower()
        
        if user_input_sort == "back":
            break
        
        elif user_input_sort in ["quick", "quick()", "quick_sort", "quick_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(int, input().split()))
                sorted_list = quick_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_sort in ["bubble", "bubble()", "bubble_sort", "bubble_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(int, input().split()))
                sorted_list = bubble_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_sort in ["count", "count()", "count_sort", "count_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(int, input().split()))
                sorted_list = count_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_sort in ["radix", "radix()", "radix_sort", "radix_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(int, input().split()))
                sorted_list = radix_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_sort in ["bucket", "bucket()", "bucket_sort", "bucket_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(float, input().split()))
                sorted_list = bucket_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_sort in ["heap", "heap()", "heap_sort", "heap_sort()"]:
            print("Введите набор чисел через пробел (например: 1 3 5 6 2):")
            try:
                unsorted_list = list(map(int, input().split()))
                sorted_list = heap_sort(unsorted_list)
                print(f"Отсортированный список: {sorted_list}\n")
            except:
                print("Неверный ввод\n")
        
        else:
            print("Неверная команда. Доступные методы: quick, bubble, count, radix\n")

def factorial_processing():
    """Функция обработки факториала"""
    while True:
        user_input_fact = input("Если хотите воспользоваться рекурсивной функцией, введите 1. Если нет, то введите 0 или back для выхода: ").strip()
        
        if user_input_fact.upper() == "BACK":
            break
        
        elif user_input_fact == "0":
            try:
                num = int(input("Введите число для вычисления факториала: "))
                if num < 0:
                    print("Ошибка: факториал отрицательного числа не определен\n")
                else:
                    ans = factorial(num)
                    print(f"Факториал {num}! = {ans}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_fact == "1":
            try:
                num = int(input("Введите число для вычисления факториала: "))
                if num < 0:
                    print("Ошибка: факториал отрицательного числа не определен\n")
                else:
                    ans = factorial_recursive(num)
                    print(f"Факториал {num}! = {ans}\n")
            except:
                print("Неверный ввод\n")
        
        else:
            print("Неверный ввод. Введите 0, 1 или back\n")

def fibonacci_processing():
    """Функция обработки фибоначчи"""
    while True:
        user_input_fibo = input("Введите 1 для рекурсивной функции, 0 для итеративной, или back для выхода: ").strip()
        
        if user_input_fibo.upper() == "BACK":
            break
        
        elif user_input_fibo == "0":
            try:
                num = int(input("Введите номер числа Фибоначчи: "))
                if num < 0:
                    print("Ошибка: номер должен быть неотрицательным\n")
                else:
                    ans = fibo(num)
                    print(f"Число Фибоначчи под номером {num} = {ans}\n")
            except:
                print("Неверный ввод\n")
        
        elif user_input_fibo == "1":
            try:
                num = int(input("Введите номер числа Фибоначчи: "))
                
                if num < 0:
                    print("Ошибка: номер должен быть неотрицательным\n")
                else:
                    ans = fibo_recursive(num)
                    print(f"Число Фибоначчи под номером {num} = {ans}\n")
            except:
                print("Неверный ввод\n")
        
        else:
            print("Неверный ввод. Введите 0, 1 или back\n")