class Person():
    def get_person(self):
        print('Enter your first name: ')
        self.first_name = input()
        print('Enter your last name: ')
        self.last_name = input()

    def print_person(self):
        print(f"You're: {self.first_name} {self.last_name}")
