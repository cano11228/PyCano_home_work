#Домашка з числами
#а
#функція яка приймає число і повертає його квадрат.
def degree_of_two(n):
    return n ** 2


# Обробка помилки, коли користувач ввів не число
try:
    num1 = float(input("Введіть число щоб дізнятися його квадрат: "))
    print(f"Результат:{degree_of_two(num1)}")
except ValueError:
    print("Ви ввели неправильне значення. Будь ласка, введіть число.")

#b
#Функція для сумми числ
def sum_numbers(num1, num2):
    return num1 + num2

try:
    num_sum1 = float(input("Введіть перше число для додавання: "))
    num_sum2 = float(input("Введіть друге число для додавання: "))
    print(f"Результат:{sum_numbers(num_sum1, num_sum2)}")
except ValueError:
    print("Ви ввели неправильні значення. Будь ласка, введіть числа")


#c
#Функція яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
def division_of_numbers(num1, num2):
    return num1 / num2

try:
    num_div1 = float(input("Введіть перше число для ділення: "))
    num_div2 = float(input("Введіть друге число на яке будем ділити перше: "))
    print(f"Результат:{division_of_numbers(num_div1, num_div2)}")
except ValueError:
    print("Ви ввели неправильні значення. Будь ласка, введіть числа")


