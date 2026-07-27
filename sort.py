import random
point = [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]]
random.shuffle(point)
print(point)
print(sorted(point))

def get_matrix():
    matrix = []

    number_of_rows = int(input("Enter number of rows: "))
    for row in range(number_of_rows):
        s = input(f"Enter row {str(row + 1)}: ")
        matrix.append([float(x) for x in s.split()])
    return matrix

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)
    return total


def main():
    m = get_matrix()
    print(m)
    print(f"\nSum of all elements is {accumulate(m)}")

main()