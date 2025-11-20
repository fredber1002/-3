class Employee:
    def __init__(self, name, id):
        self._name = name        
        self._id = id

    def get_salary(self):
        return 0

    def get_info(self):
        return f"Employee Name: {self._name}, ID: {self._id}"
    
#    /////////////////////
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, id, hourly_rate):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self._hours_worked = 0

    def add_hours(self, hours):
        self._hours_worked += hours

    def get_salary(self):
        salary = self.hourly_rate * self._hours_worked
        self._hours_worked = 0
        return salary

class SalariedEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return self.monthly_salary



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Employee:
    def get_info(self):
        pass

    def get_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, rate, hours):
        self.name = name
        self.rate = rate
        self.hours = hours

    def get_info(self):
        return "Почасовой сотрудник: " + self.name

    def get_salary(self):
        return self.rate * self.hours

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return "Сотрудник с окладом: " + self.name

    def get_salary(self):
        return self.salary

def print_payroll(employees):
    for emp in employees:
        print(emp.get_info())
        print("Зарплата:", emp.get_salary())
        print("----------------------")

workers = [
    HourlyEmployee("Иван", 300, 100),
    SalariedEmployee("Мария", 50000)
]

print_payroll(workers)
