from person import Person
from employee import Employee
from candidate import Candidate


class EmployeeReportGenerator:
    def employee_report_generator(self):
        if Candidate.dismissal_reason == 'Working':
            print(
                f'{Person.id} | {Employee.company_name[Person.id]} | {Person.full_name[Person.id]} | {Person.job_salary[Person.id]}')
        else:
            print('You are not an employee')


class CandidateReportGenerator:
    def candidate_report_generator(self):
        if Candidate.dismissal_reason != 'Working':
            print(
                f'{Person.id} | {Person.job_title[Person.id]} | {Person.full_name[Person.id]} | {Person.job_salary[Person.id]}')
        else:
            print('You are not a candidate')
