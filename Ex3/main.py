from display import Display
from userfactory import UserFactory
from reportgenerator import EmployeeReportGenerator, CandidateReportGenerator


class Main(Display, UserFactory, EmployeeReportGenerator, CandidateReportGenerator):
    def __init__(self):
        return None


main = Main()
main.get_candidate()
main.get_employee()
print(main.full_name)
main.display()
main.candidate_report_generator()
