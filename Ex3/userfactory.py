from faker import Faker
from random import randint
from person import Person
from employee import Employee


class UserFactory:
    def get_candidate(self):
        fake = Faker()
        for i in range(randint(4, 9)):
            Person.full_name.append(fake.name())
            Person.job_title.append(fake.job())
            Person.job_salary.append(randint(0, 10000))

    def get_employee(self):
        fake = Faker()
        for i in range(randint(0, 9)):
            Employee.company_name.append(fake.company())
            Employee.company_country.append(fake.country())
            Employee.company_city.append(fake.city())
            Employee.company_address.append(fake.address())
