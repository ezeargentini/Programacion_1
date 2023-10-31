class Contact:
    def __init__(self,name,phone,email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email
    
    @name.setter
    def name(self,new_name):
        self.__name = new_name
    
    @phone.setter
    def phone(self,new_phone):
        self.__phone = new_phone

    @email.setter
    def email(self,new_email):
        self.__email = new_email
        