# 1 #####

def popular_words(text, words):
    res_dict = {}

    text_list = text.casefold().rsplit(" ")

    for word in words:
        count_el = text_list.count(word)
        res_dict[word] = count_el

    return res_dict


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

##########################################
print("")
##########################################

# 2 #####


def difference(*args):

    if len(args) == 0:
        res = 0
    else:
        dif = max(*args) - min(*args)
        res = round(dif, 2)

    return res


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
