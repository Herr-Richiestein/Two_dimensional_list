import random
class GetShuffle:
    def __init__(self):
        pass

    def shuffle(self):
        my_list = []
        for i in range(100):
            char = random.randint(0, 100)
            my_list.append(char)
        print(my_list)
        d = my_list.__getitem__(2)
        my_list.index()
        for j in my_list:
            k = my_list[j]
        return my_list, my_list[2]