import random

number = int(input("Enter a number: "))
my_list = []
for row in range(number):
    my_list.append([])
    for column in range(number):
        element = random.randint(0, 9)
        my_list[row].append(element)
    print(f"{my_list[row]}")
with open("two_d_list.txt", "w") as file:
    number = int(file.read())