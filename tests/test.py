import pytest

from src.Factorial_and_Fibonacci import *
from src.Sorting import *
from src.Stack import Stack

def testfactorial():
    """Тесты факториала"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    
def testfactorial_recursive():
    """Тесты рекурсивного факториала"""
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800

def testfibonacci():
    """Тесты фибоначчи"""
    assert fibo(1) == 0
    assert fibo(2) == 1
    assert fibo(5) == 3
    assert fibo(10) == 34

def testfibonacci_recursive():
    """Тесты для рекурсивного фибоначчи"""
    assert fibo_recursive(1) == 0
    assert fibo_recursive(2) == 1
    assert fibo_recursive(5) == 3
    assert fibo_recursive(10) == 34


def testbubble_sort():
    """Тесты для bubble_sort"""
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([5, -3, 1, 4, 2]) == [-3, 1, 2, 4, 5]



def testquick_sort():
    """Тесты для quick_sort"""
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]
    assert quick_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]



def testcount_sort():
    """Тесты для count_sort"""
    assert count_sort([]) == []
    assert count_sort([5]) == [5]
    assert count_sort([5, -3, 1, 4, 2]) == [-3, 1, 2, 4, 5]



def testradix_sort():
    """Тесты для radix_sort"""
    assert radix_sort([]) == []
    assert radix_sort([5]) == [5]

    assert radix_sort([5, -3, 1, 4, 2]) == [-3, 1, 2, 4, 5]



def test_bucket_sort_empty():
    """Тесты для bucket_sort"""
    assert bucket_sort([]) == []
    assert bucket_sort([5.5]) == [5.5]
    assert bucket_sort([0.5, -0.3, 0.1, 4.5, 0.2]) == [-0.3, 0.1, 0.2, 0.5, 4.5]

def testheap_sort():
    """Тесты для heap_sort"""
    assert heap_sort([]) == []
    assert heap_sort([5]) == [5]
    assert heap_sort([5, -3, 1, 4, 2]) == [-3, 1, 2, 4, 5]

def testpush():
    """Тесты для stack.push"""
    stack = Stack()
    stack.push(5)
    assert len(stack) == 1

def testpeek():
    """Тесты для stack.peek"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20

def testpop():
    """Тесты для stack.pop"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    pop = stack.pop()
    assert pop == 20
    assert len(stack) == 1

def testmin():
    """Тесты для stack.min"""
    stack = Stack()
    stack.push(10)
    stack.push(3)
    stack.push(5)

    assert stack.min() == 3

def testlen():
    """Тесты для stack.__len__"""
    stack = Stack()
    stack.push(4)
    stack.push(3)
    assert stack.__len__() == 2