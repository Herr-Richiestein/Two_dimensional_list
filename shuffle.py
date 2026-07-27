import random
def shuffle():
    my_list = []
    for i in range(100):
        char = random.randint(0, 100)
        my_list.append(char)
    print(my_list)

def main():
    shuffle()

main()