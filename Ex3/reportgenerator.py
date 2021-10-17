import random

from person import Person
from employee import Employee
from candidate import Candidate


class EmployeeReportGenerator:
    def bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self) - 1):
                i = int(i - 1)
                if self[i] > self[i + 1]:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    swapped = True

    def employee_report_generator(self):
        if Candidate.dismissal_reason == 'Working':
            Person.job_salary.sort(reverse=True)
            Employee.company_name.sort()
            self.result = [Person.id, Employee.company_name[Person.id], Person.full_name[Person.id],
                           Person.job_salary[Person.id]]
            print(self.result)
        else:
            print('You are not an employee')


class CandidateReportGenerator:
    def candidate_report_generator(self):
        if Candidate.dismissal_reason != 'Working':
            print(
                f'{Person.id} | {Person.job_title[Person.id]} | {Person.full_name[Person.id]} | {Person.job_salary[Person.id]}')
        else:
            print('You are not a candidate')
