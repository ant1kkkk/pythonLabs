from person import Person


class Client(Person):
    def __init__(self, service, price):
        self.service = service
        self.price = price

    def print_person(self):
        print(f"You're: {self.first_name} {self.last_name}. Your price is {self.price}")
