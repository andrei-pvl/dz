my_input = int(input("Input 4-elements number: "))
inputted_input = f"Inputted number: {my_input}"
print(inputted_input)

my_input1 = my_input//1000
print(my_input1)

my_input2 = my_input%1000//100
print(my_input2)

my_input3 = my_input%1000%100//10
print(my_input3)

my_input4 = my_input%1000%100%10//1
print(my_input4)

print("Hillel Top!")