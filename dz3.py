# 1 ########

first_input = float(input("Input first element: "))
second_input = float(input("Input second element: "))

input_operation = input("Input operation(+, -, *, /): ")

if input_operation == "+":
    result_input = first_input + second_input
    print(f"Result = {result_input}")
elif input_operation == "-":
    result_input = first_input - second_input
    print(f"Result = {result_input}")
elif input_operation == "*":
    result_input = first_input * second_input
    print(f"Result = {result_input}")
elif input_operation == "/":
    if second_input != 0:
        result_input = first_input / second_input
        print(f"Result = {result_input}")
    else:
        print("Error second_input")
else:
    print("Error operation")

##########################################
print("")
##########################################

# 2 ########

#my_list = [12, 3, 4, 10]
#my_list = []
my_list = [5]
#my_list = [12, 3, 4, 10, 8]

copy_list = my_list.copy()

if len(copy_list) == 0 or len(copy_list) == 1:
    print(f" {my_list} => {copy_list}")
else:
    first_element = copy_list.pop(-1)
    copy_list.insert(0, first_element)
    print(f" {my_list} => {copy_list}")
