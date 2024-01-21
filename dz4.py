# 1 ########

my_list1 = [0, 1, 0, 12, 3]
# my_list = [0]
# my_list = [1, 0, 13, 0, 0, 0, 5]
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(my_list1)
index = 0

while index < len(my_list1):
    if my_list1[index] == 0:
        my_list1.append(0)
        my_list1.remove(0)
    index += 1
print(my_list1)

##########################################
print("")
##########################################

# 2 ########

my_list2 = [0, 1, 7, 2, 4, 8]
# my_list2 = [1, 3, 5]
# my_list2 = [6]
# my_list2 = []

print(my_list2)

if len(my_list2) == 0:
    res = 0
else:
    sum_el = sum(my_list2[::2])
    res = sum_el * my_list2[-1]
print(res)
