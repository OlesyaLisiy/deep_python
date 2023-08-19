# Напишите код, который запрашивает число и сообщает является ли оно
# простым или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime():
    num = int(input("Введите число: "))

    if num < 0 or num > 100000:
        print("Введено недопустимое число. Допустимы числа от 0 до 100000.")

    else:
        if num == 1 or num == 0:
            print("Число не является ни простым, ни составным.")

        else:
            i = 2
            while i < num:
                if num % i != 0:
                    print("Число простое")
                else:
                    print("Число составное.")
                    break
                i += 1


is_prime()