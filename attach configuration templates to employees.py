class Employee:
    def _init_(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.salary_config = None 

    def attach_salary_config(self, salary_config):

        if not isinstance(salary_config, SalaryConfig):
            raise TypeError("Argument must be a SalaryConfig object")
        self.salary_config = salary_config

class SalaryConfig:
    def _init_(self, config_id, base_salary, benefits, deductions):
        self.config_id = config_id
        self.base_salary = base_salary
        self.benefits = benefits  
        self.deductions = deductions 

    def calculate_net_salary(self):
        """Calculates the employee's net salary based on the configuration.

        Returns:
            float: The employee's net salary.
        """

        total_benefits = sum(self.benefits.values())
        total_deductions = sum(self.deductions.values())
        return self.base_salary + total_benefits - total_deductions
    
emp1 = Employee("Arooj Fatima", 123)
salary_config1 = SalaryConfig(101, 500000, {"Health Insurance": 1000, "Travel Allowance": 5000}, {"Tax": 2000})
emp1.attach_salary_config(salary_config1)

net_salary = emp1.salary_config.calculate_net_salary()
print(f"Employee Name: {emp1.name}")
print(f"Net Salary: {net_salary}")    