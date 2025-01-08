class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f'имя: {self.name}, ID: {self.id}'

    
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        return f'{self.name} управленец: {self.department}'
    
    def get_info(self):
        info = Employee.get_info(self)
        return f'{info}, отдел: {self.department}'


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} обслуживает: {self.specialization}'
    
    def get_info(self):
        info = Employee.get_info(self)
        return f'{info}, специлизация: {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return f'{self.name} нет рабочих'
        info = f'команда {self.name}:\n'
        for emp in self.team:
            info += f'- {emp.get_info()}\n'
        return info
    def get_info(self):
        info = Manager.get_info(self)
        return f'{info}, специализация: {self.specialization}'
    
employee = Employee("Никита Аведеев", "1")
manager = Manager("Алексей МИхайлович", "2", "актер")
technician = Technician("Людила Фёдоровна", "3", "создатель")
tech_manager = TechManager("Сергей Какошка", "4", "Ютуб", "монтажёр")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project())
print(technician.get_info())
print(technician.perform_maintenance())
print(tech_manager.get_info())
tech_manager.add_employee(employee)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())