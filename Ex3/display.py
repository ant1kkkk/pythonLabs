from person import Person
from candidate import Candidate
from employee import Employee
from userfactory import UserFactory


class Display(Employee, Candidate, Person):
    def display(self):
        print("id since 1: ")
        Person.id = int(input())
        Candidate.dismissal_reason = Candidate.dismissal_reasons(self)
        if Candidate.dismissal_reason != 'Null' and Candidate.dismissal_reason != 'Working':
            print(f'''Hello, I am {Person.full_name[Person.id]}.
                    I want to be a {Person.job_title[Person.id]} with a salary from {Person.job_salary[Person.id]}.
                    I quit my previous job for a reason of {Candidate.dismissal_reason}''')
        elif Candidate.dismissal_reason == 'Null':
            print(f'''Hello, I am {Person.full_name[Person.id]}.
                    I want to be a {Person.job_title[Person.id]} with a salary from {Person.job_salary[Person.id]}.
                    I haven't worked anymore before.''')
        elif Candidate.dismissal_reason == 'Working':
            print(
                f'''Hello, I am {Person.full_name[Person.id]}, {Person.job_title[Person.id]} in {Employee.company_name[Person.id]}
                    ({Employee.company_country[Person.id]}, {Employee.company_city[Person.id]}, 
                    {Employee.company_address[Person.id]}),  and my salary {Person.job_salary[Person.id]} ''')
