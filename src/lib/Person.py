class Person:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    def getFullName(self):
        """
        Returns:\n
            formatted string of self.__first + self.__last
        """
        return f"{self.__first} {self.__last}"

    def getFirstName(self):
        """
        Returns:\n
            -> self.__first
        """
        return self.__first

    def getLastName(self):
        """
        Returns:\n
            self.__last
        """
        return self.__last