# 1 #####

def add_one(some_list):
    str_el = ""
    index1 = 0
    index2 = 0
    res_list = []

    while index1 < len(some_list):
        str_el += str(some_list[index1])
        index1 += 1

    res_el = str(int(str_el) + 1)

    while index2 < len(res_el):
        res_list.append(int(res_el[index2]))
        index2 += 1

    return res_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

##########################################
print("")
##########################################

# 2 #####


def find_unique_value(some_list):
    index = 0
    uniq_el = 0

    while index < len(some_list):

        if some_list.count(some_list[index]) == 1:
            uniq_el = some_list[index]
        index += 1

    return uniq_el


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
