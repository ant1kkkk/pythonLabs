from person import Person
from candidate import Candidate
from employee import Employee

class Display(Person, Employee):
    def display(self):
        self.reason = self.dismissal_reasons()
        if self.reason != ('Null' and 'Working'):
            print(f'''Hello, I am {self.full_name()}.
                    I want to be a {self.job_title} ({self.job_description}) with a salary from {self.job_salary}.
                    I quit my previous job for a reason of {self.reason}''')
        elif self.reason == 'Null':
            print(f'''Hello, I am {self.full_name()}.
                    I want to be a {self.job_title} ({self.job_description}) with a salary from {self.job_salary}.
                    I haven't worked anymore before.''')
        elif self.reason == 'Working':
            print(f'''Hello, I am {self.full_name()}, {self.job_title} in {self.company_name}
                    ({self.company_country}, {self.company_city}, {self.company_address}), and my 
                    salary {self.job_salary} ''')
Tom = Display()
Tom.display()