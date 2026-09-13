class Customer:
    def __init__(self, firstName, lastName):
        self.first = firstName
        self.last = lastName

    def getFirstName(self):
        return self.first

    def getLastName(self):
        return self.last

    def getFullName(self):
        return f"{self.first} {self.last}"