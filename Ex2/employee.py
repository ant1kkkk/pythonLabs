from person import Person


class Employee(Person):
    def __init__(self, specialization):
        self.specialization = specialization

    def __get_deduction(self):
        return float((self.salary_per_hour * 14) / 100)

    def get_salary(self):
        print("How long is your working day?: ")
        self.worker_day = int(input())
        print("How many days in month did you worked?: ")
        self.number_of_days = int(input())
        print("What is your salary per hour?: ")
        self.salary_per_hour = int(input())
        self.salary = (((self.salary_per_hour - self.__get_deduction()) * self.worker_day) * self.number_of_days)
        return self.salary

    def print_person(self):
        print(f"You're: {self.first_name} {self.last_name}. Your price is {self.get_salary()}")
