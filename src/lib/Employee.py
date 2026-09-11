from .Person import Person

class Employee(Person):
    def __init__(self, first: str, last: str, employeeID: int, salary: float = 0, performance: float = 0):
        super().__init__(first, last)
        self.employeeID = employeeID
        self.salary = salary
        self.performance = performance

    def getEmployee(self) -> dict:
        """
        Returns:\n 
            Dictionary value of employee
        """
        return {
            'full_name': self.getFullName(),
            'first_name': self.getFirstName(),
            'last_name': self.getLastName(),
            'employeeID': self.employeeID,
            'salary': self.salary,
            'performance': self.performance
        }

    def updatePerformance(self, performance: float) -> None:
            self.performance = performance

    def updateCertificates(self):
        pass

    def updateSalary(self, value: float) -> None:
        self.salary = value

    def updateName(self, firstName: str, lastName: str) -> None:
        if self.__first == firstName:
            pass
        else:
            self.__first = firstName

        if self.__last == lastName:
            pass
        else:
            self.__last = lastName