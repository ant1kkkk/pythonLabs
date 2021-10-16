from person import Person
from candidate import Candidate
from employee import Employee


class Display(Person, Employee, Candidate):
    def display(self):
        print("id since 0: ")
        self.id = int(input())
        self.reason = self.dismissal_reasons()
        if self.reason != 'Null' and self.reason != 'Working':
            print(f'''Hello, I am {self.full_name[self.id]}.
                    I want to be a {self.job_title[self.id]} with a salary from {self.job_salary[self.id]}.
                    I quit my previous job for a reason of {self.reason}''')
        elif self.reason == 'Null':
            print(f'''Hello, I am {self.full_name[self.id]}.
                    I want to be a {self.job_title[self.id]} with a salary from {self.job_salary[self.id]}.
                    I haven't worked anymore before.''')
        elif self.reason == 'Working':
            print(f'''Hello, I am {self.full_name[self.id]}, {self.job_title[self.id]} in {self.company_name[self.id]}
                    ({self.company_country[self.id]}, {self.company_city[self.id]}, {self.company_address[self.id]}), 
                    and my salary {self.job_salary[self.id]} ''')
