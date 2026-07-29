import statistics as st

avg_hours_list = []

def average_daily_hours(employee_list):
    for i in range(len(employee_list)):
        avg_hour = [round(st.mean(employee_list[i]), 2), i + 1]
        avg_hours_list.append(avg_hour)
    avg_hours_list.sort(reverse=True)

    for employees in avg_hours_list:
        print(f"Employee {employees[1]} worked an average of {employees[0]} hours in a day")


def main():
    employee_list = []
    for employee in range(3):
        hours = input(
            f"Enter the number of hours employee {employee + 1} worked from Sun - Sat, separated by space: ").strip().split()
        employee_list.append([float(x) for x in hours])
    print("")

    average_daily_hours(employee_list)


main()