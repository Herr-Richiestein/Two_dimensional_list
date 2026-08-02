my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [str(x) for x in my_list]
for i in range(len(list1)):
    print("".join(list1[i]), end=" ")