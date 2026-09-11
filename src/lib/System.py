from .Employee import Employee

class System:
    def __init__(self, employeeCount: int = 0, employees: list[Employee] = []):
        self.employeeCount: int = employeeCount
        self.employees: list[Employee] = employees
        self.employeeIDS = 1

    def printMenu(self) -> None:
        print(f"{'=' * 20}MENU{'=' * 20}\n"                     \
        "[1] Add Employee\n"                                    \
        "[2] Remove Employee\n"                                 \
        "[3] Update Employee Information\n"                     \
        "[4] Update Employee Performance\n"                     \
        "[5] Update Employee Salary\n"                          \
        "[6] View Employee List\n"                              \
        "[7] View Metrics\n"                                    \
        "[8] EXIT\n"                                            \
        f"{'=' * 44}\n")

    def viewMetrics(self) -> None:
        meanSalary      = 0
        medianSalary    = 0
        modeSalary      = 0
        print(f"{"=" * 15}METRICS{"=" * 15}\n"                      \
            f"TOTAL EMPLOYEE COUNT: {self.employeeCount}\n"         \
            f"EMPLOYEES (FIRST 3): []\n"                            \
            f"TOP (3) PERFORMING EMPLOYEES: []\n"                   \
            f"EMPLOYEE SALARY (MEAN): {meanSalary}\n"               \
            f"EMPLOYEE SALARY (MEDIAN): {medianSalary}\n"           \
            f"EMPLOYEE SALARY (MODE): {modeSalary}\n"               \
        f"{'=' * 37}\n")

    def viewEmployees(self) -> None:
        """
        Gets list of employees printed as a table
        """
        print(f'{'=' * 13}EMPLOYEE-LIST{'=' * 13}')
        if len(self.employees) <= 0:
            print("NO EMPLOYEES")
        else:
            print(f"{'EMPLOYEE-ID':<15} | {'FULLNAME':<25} | {'SALARY':<12} | {'PERFORMANCE':<15}")
            print("-" * 90)
            for e in self.employees:
                employee = e.getEmployee()
                print(f"{employee['employeeID']:<15} | {employee['full_name']:<25} | {employee['salary']:<12} | {employee['performance']}{'%':<15}")
        print(f'{'=' * 39}\n')

    def mapInput(self, x: int) -> bool:
        """
        This maps user input 'x' to a specific case (switch casing)\n
        Returns:\n
            bool -> True if x not equal to the value 'Exit'
        Parameters:\n
            int -> x is a user input
        """
        match x:
            case 1: # Add Employees
                firstName = input("Input first name: ")
                lastName = input("Input last name: ")
                self.employees.append(Employee(firstName, lastName, self.employeeIDS))
                print(f"[Success]: Successfully created employee no. {self.employeeIDS}\n")
                self.employeeIDS += 1
                self.employeeCount += 1
                return True
            case 2: # Remove Employee
                if (self.employeeCount == 0):
                    print(f"[Error]: Unable to remove employee when employee count is {self.employeeCount}")
                    pass
                else:
                    eID = int(input("Input Employee ID: "))
                    print(f"[Success]: Successfully removed employee no. {eID}\n")
                    pass
            case 3: # Update Info
                eID = int(input("Input Employee ID: "))
                print(f"[Success]: Successfully updated employee no. {eID}'s information\n")
                return True
            case 4: # Update Performance
                eID = int(input("Input Employee ID: "))
                print(f"[Success]: Successfully updated employee no. {eID}'s performance\n")
                return True
            case 5: # Update Salary
                eID = int(input("Input Employee ID: "))
                print(f"[Success]: Successfully updated employee no. {eID}'s salary\n")
                return True
            case 6: # View Employee List
                self.viewEmployees()
                return True
            case 7: # View Metrics
                self.viewMetrics()
                return True
            case 8: # Exit
                return False
 
    def initializeSystem(self) -> None:
        """
            Initializes the system, also Maps User Input to the MENU\n
            Args:\n
                None
            Returns:\n
                None
        """
        while True:
            self.printMenu()
            try:
                user_input = int(input("INPUT: "))
            except ValueError:
                print(f"[Error]: could not convert input to an INTEGER. Please enter a NUMBER\n")
                continue

            cont = self.mapInput(user_input)
            if not cont:
                break
                