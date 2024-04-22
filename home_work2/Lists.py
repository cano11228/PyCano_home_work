#Домашка з списками
#a
#функція для обчислення середнього значення списку чисел.
list1 = [1,2,3,4,5,6,7,8]
def average_value(list):
    return sum(list)/len(list)

print(f"Середнє значення списку чисел:{average_value(list1)}")


#b
#функція, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
list2 = ["aplle", 23, 544, True]
list3 = ["sd" , 34, 23, True, "aplle"]
def common_elements(list, list1):
    return set(list).intersection(set(list1))

new_list = common_elements(list3, list2)
print(f"Збіги елементів в двох списках:{new_list}")


