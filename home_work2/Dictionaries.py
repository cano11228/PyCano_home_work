#Домашка з словниками
fruits = {
    'orange':'orange',
    'apple': 'red',
    'banana': 'yellow',
}
vegetables = {
    'carrot': 'orange',
    'tomato': 'red',
    'cucumber': 'green'
}
#a
#функція, яка приймає словник і виводить всі ключі цього словника.
def get_key(dict):
    return dict.keys()

print(f"Ключі зі словника fruits: {get_key(fruits)}")

#b
#функція, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників
def sum_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result
print(f"Обєднання двох списків fruits і vegetables: {sum_dicts(fruits, vegetables)}")