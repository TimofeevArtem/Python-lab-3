class Stack:
    """Класс стека"""
    def __init__(self):
        """Функция инициализирует стек"""
        self.stack = []

    def push(self, x: int) -> None:
        """Функция добавляет элемент в стек"""
        self.stack.append(x)
    
    def pop(self) -> int:
        """Функция удаляет верхний элемент стека"""
        return self.stack.pop()
    
    def peek(self) -> int:
        """Функция возвращает верхний элемент стека"""
        return(self.stack[-1])
        
    def min(self) -> int:
        """Функция возвращает минимальный элемент в стеке"""
        return min(self.stack)
    
    def __len__(self) -> int:
        """Функция возвращает количество элементов в стеке"""
        return len(self.stack)
    
    def is_empty(self) -> bool:
        """Функция проверяет пустой ли стек"""
        if len(self.stack) == 0:
            return True
        else:
            return False