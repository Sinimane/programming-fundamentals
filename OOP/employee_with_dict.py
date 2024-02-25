employee1 = {
    "name": "Ji-Soo",
    "age": 38,
    "position": "developer",
    "salary": 1200
}
employee2 = {
    "name": "Lauren",
    "age": 44,
    "position": "tester",
    "salary": 1000
}

def init_employee(name, age, position, salary):
    return {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary
    }

def employee_info(e):
    print(f"Employee {e["name"]} salary is {e["salary"]}")


def increase_employee_salary(e, percent):
    e["salary"] +=  e["salary"] * percent/100


def main():
    employees = [employee1, employee2]
    employee3 = init_employee("Sarah", 34, "Manager", 2300)
    employees.append(employee3)

    for e in employees:
        increase_employee_salary(e, 20)
        employee_info(e)


main()
