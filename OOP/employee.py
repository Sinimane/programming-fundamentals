class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def info(self):
        print(f"{self.name} is {self.age} old. He is working as {self.position} for a salary of {self.salary}")

    def increase_salary(self, percent):
        self.salary += self.salary * percent/100


class Developer(Employee):

    def __init__(self, name, age, position, salary, languages):
        super().__init__(name, age, position, salary)
        self.languages = languages

    def list_programming_languages(self):
        print(f"{self .name} programming Languages are: {self.languages}")

    def increase_salary(self, percent, bonus=400):
        self.salary += self.salary * percent/100
        self.salary += bonus


def main():
    #employee1 = Employee("Ji-Soo", 38, "tester", 1200)
    #employee1.info()

    dev1 = Developer("Carl", 23, "Developer", 3220, ["Java", "Python", "JS"])
    dev1.info()
    dev1.list_programming_languages()
    dev1.increase_salary(10)
    dev1.info()


main()