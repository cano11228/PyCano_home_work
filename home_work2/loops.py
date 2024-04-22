#Домашка по циклах
#a
#функція, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
def check_even_odd(number):
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

#Приклад:
num = 5
check_even_odd(num)

#b
#функція, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)
