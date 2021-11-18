"""
Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
Sample Dictionary :
dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
final_dict = {}

dict_list = (dict_1, dict_2, dict_3)
for dictionary in dict_list:
    final_dict.update(dictionary)
print(final_dict)

# check the invariability of the initial data
assert dict_1 == {1: 10, 2: 20}
assert dict_2 == {3: 30, 4: 40}
assert dict_3 == {5: 50, 6: 60}

