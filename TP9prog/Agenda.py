from Contact import Contact
class Agenda:
    def __init__(self):
        self.contacts = []

    def add_contacts(self,name,phone,email):
        contact = Contact(name,phone,email)
        self.contacts.append(contact)

    def display_contact(self):
        for contact in self.contacts:
            print(f'Nombre: {contact.name}')
            print(f'Phone: {contact.phone}')
            print(f'Email: {contact.email}')

    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                print(f'Nombre: {contact.name}')
                print(f'Phone: {contact.phone}')
                print(f'Email: {contact.email}')

    def update_contact(self,name,new_phone,new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                print("El contacto fue modificado con exito")
                return
        print(f'{name} no fue encontrado en la agenda')                

