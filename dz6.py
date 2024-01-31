# 1 #####

people_list = [{"name": "John", "age": 65},
               {"name": "Jack", "age": 45},
               {"name": "Andriy", "age": 18},
               {"name": "Ann", "age": 45},
               {"name": "Arkadiy", "age": 34},
               ]

min_age = people_list[0]['age']
max_len = 0
list_a = []
list_b = []
list_c = []

for person in people_list:
    age = int(person['age'])
    len_name = len(person['name'])

    if age < min_age:
        list_a = [person['name']]
        min_age = age
    elif age == min_age:
        list_a.append(person['name'])

    if len_name > max_len:
        list_b = [person['name']]
        max_len = len_name
    elif len_name == max_len:
        list_b.append(person['name'])

    list_c.append(age)

avg_age = sum(list_c) / len(list_c)

print(list_a)
print(list_b)
print(avg_age)

##########################################
print("")
##########################################

# 2 #####

my_dict_1 = {"name": "Alice", "age": 30, "city": "New York", "status": "married", "kids": "3"}
my_dict_2 = {"name": "John", "age": 65, "city": "New York", "status": "unmarried"}

my_dict_3 = {}
my_dict_4 = {}

value_set_1 = set(my_dict_1.keys())
value_set_2 = set(my_dict_2.keys())

res_list_1 = list(value_set_1.intersection(value_set_2))
res_list_2 = list(value_set_1.difference(value_set_2))

for key in my_dict_1:
    if key not in my_dict_2:
        my_dict_3[key] = my_dict_1[key]


for key1, value1 in my_dict_1.items():
    for key2, value2 in my_dict_2.items():
        if key1 not in my_dict_2:
            my_dict_4[key1] = my_dict_1[key1]
        if key2 not in my_dict_1:
            my_dict_4[key2] = my_dict_2[key2]
        elif key1 == key2:
            my_dict_4[key1] = [my_dict_1[key1], my_dict_2[key2]]


print(res_list_1)
print(res_list_2)
print(my_dict_3)
print(my_dict_4)
