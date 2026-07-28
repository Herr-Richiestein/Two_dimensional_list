def max_column(matrix, column_index):
    column_list = []
    for row in matrix:
        column_list.append(row[column_index])
    print(f"Maximum of elements at column {column_index} is {max(column_list)}")

def main():
    a = int(input("Enter the number of rows: "))
    b = int(input("Enter the number of columns: "))
    row = []
    for i in range(a):
        string_row = input(f"Enter {a} x {b} matrix row {i}: ").strip().split(",")
        row.append([int (x) for x in string_row])
    print("")

    for column in range(b):
        max_column(row, column)
main()