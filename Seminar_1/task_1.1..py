# Задача 1.1
# Треугольник существует только тогда, когда сумма любых двух
# его сторон больше третьей. Дано a, b, c - стороны предполагаемого
# треугольника. Требуется сравнить длину каждого отрезка-стороны с
# суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник с такими сторонами не существует")

    # Определение типа треугольника
    elif a != b and b != c and a != c:
        print("Треугольник разносторонний")
    elif a == b and b == c:
        print("Треугольник равносторонний")
    else:
        print("Треугольник равнобедренный")


a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
triangle_type(a, b, c)
