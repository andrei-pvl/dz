# 1 #####
user_input = input("Enter name of variable: ")

result = False
reserved_words = ['and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                  'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None',
                  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield']
punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'

if user_input[0].isdigit():
    result = False
elif user_input.isdigit():
    result = False
elif user_input in reserved_words:
    result = False
else:
    result = True
for char in user_input:
    if char.isupper() or char.isspace() or (char in punctuation_chars and char != '_'):
        result = False

print(result)

##########################################
print("")
##########################################

# 2 #####

while True:
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

    input_continue = input("Do you want to do another calculation? (yes/no): ")

    if input_continue.lower() != 'yes':
        break
