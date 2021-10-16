from faker import Faker
from random import randint
from person import Person
from display import Display


class Main(Display, Person):
    def get_candidate(self):
        fake = Faker()
        for i in range(randint(0, 9)):
            self.full_name.append(fake.name())
            self.job_title.append(fake.job())
            self.job_salary.append(randint(0, 10000))

    def get_employee(self):
        fake = Faker()
        for i in range(randint(0, 9)):
            self.company_name.append(fake.company())
            self.company_country.append(fake.country())
            self.company_city.append(fake.city())
            self.company_address.append(fake.address())


Gay = Main()
Gay.get_candidate()
Gay.get_employee()
print(Gay.full_name)
Gay.display()
