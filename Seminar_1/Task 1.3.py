# Задача 1.3.
# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного # числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

def random_value_game():
    random_value = randint(0, 1000)
    attempt = 0
    print("Загадано число от 0 до 1000. Попробуйте отгадать за 10 попыток")
    for i in range(1,11):
        choice = int(input("Введите число: "))
        if choice > random_value:
            print("Это число больше задуманного")
        elif choice < random_value:
            print("Это число меньше задуманного")
        else:
            print(f"Верно! Количество попыток - {i}")
            break
        attempt += 1
        print(f"Осталось попыток {10-attempt}")
    if attempt >= 10:
        print(f"Попытки закончились! Было загадано {random_value}")


random_value_game()
