from display import Display
from userfactory import UserFactory


class Main(Display, UserFactory):
    def __init__(self):
        return None


main = Main()
main.get_candidate()
main.get_employee()
print(main.full_name)
main.display()
