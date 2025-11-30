from processing import *

def main():
    """Основная функция"""
    stack = Stack()

    while True:
        print("Выберите с какой структурой хотите работать (STACK, SORTING, FACTORIAL или FIBONACCI)")
        print("Если хотите выйти, введите EXIT\n")
        user_input = input().strip().upper()
        
        if user_input == "EXIT":
            print("Хорошего дня!")
            break
        
        elif user_input == "STACK":
            stack_processing(stack)
        
        elif user_input == "SORTING":
            sorting_processing()
        
        elif user_input == "FACTORIAL":
            factorial_processing()
        
        elif user_input == "FIBONACCI":
            fibonacci_processing()
        
        else:
            print("Неверный ввод. Доступные опции: STACK, SORTING, FACTORIAL, FIBONACCI, EXIT\n")

if __name__ == "__main__":
    main()