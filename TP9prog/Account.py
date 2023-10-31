from Person import Person
class Account:
    def __init__(self,person=Person(),quantity=0):
        self.__person = person
        self.__quantity = quantity

    @property
    def person(self):
        return self.__person
    
    @property
    def quantity(self):
        return self.__quantity
    
    @person.setter
    def person(self,new_person):
        self.__person = new_person

    @person.setter
    def quatity(self,new_quantity):
        self.__quantity = new_quantity

    def display_data(self):
        self.__person.display()
        print(f'Dinero: {self.__quantity}')

    def income(self,quantity_income):
        if quantity_income > 0:
            self.__quantity += quantity_income

    def to_get(self,quantity_to_get):
        self.__quantity -= quantity_to_get    



