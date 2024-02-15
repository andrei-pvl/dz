# 1 #####

def simple_num(num):
    div = 1
    div_list = []
    while div <= num:
        if num % div == 0:
            div_list.append(div)
        div += 1

    return True if len(div_list) == 2 else False


def prime_generator(end):
    number = 1
    while number <= end:
        if simple_num(number):
            yield number
        number += 1


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


##########################################
print("")
##########################################

# 2 #####


def is_even(number):
    res = False
    list_num = list(str(number))
    lists = ['0', '2', '4', '6', '8']
    for num in lists:
        if list_num[-1] == num:
            res = True

    return res


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
