set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
#домашка по сетах
#a
#функція, яка приймає дві множини і повертає їхнє об'єднання.
def union_sets(set1, set2):
    return set1.union(set2)

result = union_sets(set1, set2)
print(f"Обєднання двох сетів{result}")

#b
#функція, яка перевіряє, чи є одна множина підмножиною іншої.
def is_subset(set1, set2):
    return set1.issubset(set2)

subset1 = {1, 2, 3}
subset2 = {1, 2, 3, 4, 5}

result1 = is_subset(subset1, subset2)
print(f"Перевірка на наявність підмножин, результат перевірки повертається як результат функції. {result1}")
