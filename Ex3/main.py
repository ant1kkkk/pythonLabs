from display import Display
from userfactory import UserFactory
from reportgenerator import EmployeeReportGenerator, CandidateReportGenerator
from employee import Employee


class Main(Display, UserFactory, EmployeeReportGenerator, CandidateReportGenerator, Employee):
    def __init__(self):
        return None


main = Main()
main.get_candidate()
main.get_employee()
print(main.full_name)
main.display()
main.employee_report_generator()
