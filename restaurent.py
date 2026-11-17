from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employess = [] #items database
        self.menu = Menu()

    def add_employee(self,employee):
        self.employess.append(employee)

    def view_employee(self):
        print('Employe List')
        for emp in self.employess:
            print(emp.name, emp.phone, emp.email, emp.address, emp.age, emp.designation, emp.salary)
