class Employee:
    def __init__(self, baseSalary, overtime, rate) -> None:
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate
    
    def getWage(self):
        return self.baseSalary + (self.overtime * self.rate)
    
myWage = Employee(30000, 12, 5)

print(myWage.getWage())

