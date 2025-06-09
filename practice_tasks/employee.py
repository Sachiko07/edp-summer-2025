class Employee:
    def __init__(self, name, emp_id, role):
        self.name = name
        self.emp_id = emp_id
        self.role =role

class Vet(Employee):
    def __init__(name, emp_id, role):
        super().__init__(name, emp_id, role)
    def treat():
        print("treating animal")

class Guard(Employee):
    def __init__(name, emp_id, role):
        super().__init__(name, emp_id, role)
    def check():
        print("Checking perimeter")