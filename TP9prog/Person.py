class Person:
    def __init__(self, name='', age=0, id=0):
        self.__name = name
        self.__age = age
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    @age.setter
    def age(self,new_age):
        self.__age = new_age

    @id.setter
    def id(self,new_id):
        self.__id = new_id

    def display(self):
        print(f'Nombre: {self.__name}')
        print(f'Edad: {self.__age}')
        print(f'DNI: {self.__id}') 

    def is_of_legal_age(self):
        if self.__age > 18:
            return True
        else:
            return False
        
