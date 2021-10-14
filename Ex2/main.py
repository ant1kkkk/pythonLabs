from client import Client
from employee import Employee

client = Client('Technical assistance', 100)
client.get_person()
client.print_person()
employee = Employee('System administrator')
employee.get_person()
employee.print_person()