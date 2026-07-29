import statistics as st


def avg_major_diagonal(square):
    row = []
    for i in range(len(square)):
        row.append(square[i][i])
    average = st.mean(row)
    return f"The average of the elements in the major diagonal is {average}"


def main():
    number = int(input("Enter the number of rows which is the same as column: "))
    square = []
    for i in range(number):
        str_row = input(f"Enter the values for row {i}: ").split(",")
        square.append([float(x) for x in str_row])
    print(avg_major_diagonal(square))


main()