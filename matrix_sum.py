def add_matrix(a, b):
    c = []  # sum of matrix a and b
    for i in range(len(a)):
        element = a[i] + b[i]
        c.append(element)
    return "".join(c)


def display_matrix(a, b):
    sub_a = []
    sub_b = []
    sub_c = []

    for j in range(1, len(add_matrix(a, b)) + 1):
        sub_a.append(j - 1)
        sub_b.append(j - 1)
        sub_c.append(j - 1)

        if j % 3 == 0:
            print(f"{"".join(sub_a)}\t{"".join(sub_b)}\t{"".join(sub_c)}")
            print("")
            sub_a = []
            sub_b = []
            sub_c = []


def main():
    m1 = input("Enter all the value of 3 x 3 matrix1 on a straight line separated by space: ").strip().split()
    matrix1 = [float(x) for x in m1]

    m2 = input("Enter all the value of 3 x 3 matrix2 on a straight line separated by space: ").strip().split()
    matrix2 = [float(y) for y in m2]

    print(add_matrix(matrix1, matrix2))
    # display_matrix(matrix1, matrix2)


main()