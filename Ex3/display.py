from person import Person
from candidate import Candidate
from employee import Employee
from userfactory import UserFactory


class Display(Candidate, Employee, Person):
    def display(self):
        print("id since 0: ")
        self.id = int(input())
        Candidate.dismissal_reason = Candidate.dismissal_reasons(self)
        if Candidate.dismissal_reason != 'Null' and Candidate.dismissal_reason != 'Working':
            print(f'''Hello, I am {Person.full_name[self.id]}.
                    I want to be a {Person.job_title[self.id]} with a salary from {Person.job_salary[self.id]}.
                    I quit my previous job for a reason of {Candidate.dismissal_reason}''')
        elif Candidate.dismissal_reason == 'Null':
            print(f'''Hello, I am {Person.full_name[self.id]}.
                    I want to be a {Person.job_title[self.id]} with a salary from {Person.job_salary[self.id]}.
                    I haven't worked anymore before.''')
        elif Candidate.dismissal_reason == 'Working':
            print(
                f'''Hello, I am {Person.full_name[self.id]}, {Person.job_title[self.id]} in {Employee.company_name[self.id]}
                    ({Employee.company_country[self.id]}, {Employee.company_city[self.id]}, 
                    {Employee.company_address[self.id]}),  and my salary {Person.job_salary[self.id]} ''')
