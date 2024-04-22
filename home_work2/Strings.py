#Домашка з рядками
#a
#Фунція для перевірки довжини
def get_str(s):
    return len(s)
input_str = input(F"Введіть рядок щоб дізнатися довжину:")
input_str = input_str.replace(" ", "")
print(get_str(input_str))


#b
#Функція для додавання рядків
def adding_str(s1, s2):
    return print(s1 + s2)

input_two_str1 = input(f"Введіть перший рядок:")
input_two_str2 = input(f"Введіть другий рядок:")
adding_str(input_two_str1, input_two_str2)

