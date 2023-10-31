#Ejercicio 1

from Person import Person

person_one = Person()
name = str(input("Ingrese el nombre de la persona: "))
person_one.name = name
age = int(input("Ingrese la edad de la persona: "))
person_one.age = age
id = int(input("Ingrese el dni de la persona: "))
person_one.id = id
print("Los datos de la persona son: ")
person_one.display()
print(f'{person_one.name} es mayor de edad: {person_one.is_of_legal_age()}')

#Ejercicio 2
from Account import Account

from Person import Person

name = str(input("Ingrese el nombre del titular de la cuenta: "))
age = int(input("Ingrese la edad del titular de la cuenta: "))
id = int(input("Ingrese el dni del titular de la cuenta: "))
person = Person(name,age,id)
my_accuont = Account(person)
quantity_income = int(input("Ingrese la cantidad de dinero que desea ingresar a la cuenta: "))
my_accuont.income(quantity_income)
quantity_to_get = int(input("Ingrese la cantidad de dinero que desea retirar de la cuenta: "))
my_accuont.to_get(quantity_to_get)
my_accuont.display_data()

#Ejercicio 3
from Triangulo import Triangulo

side_1 = int(input("Ingrese el lado 1: "))
side_2 = int(input("Ingrese el lado 1: "))
side_3 = int(input("Ingrese el lado 1: "))
Triangulo = Triangulo(side_1, side_2, side_3)
print(f"El lado mas grande es {Triangulo.major_side}")
print(f"{Triangulo.triangle_type}")

#Ejercicio 4
from Agenda import Agenda

my_agenda = Agenda()

while True:
            print("Menú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            option = input("Elija una opción: ")
            if option == "1":
                name = input("Ingrese el nombre: ")
                phone = input("Ingrese el teléfono: ")
                email = input("Ingrese el correo electrónico: ")
                my_agenda.add_contacts(name, phone, email)
            elif option == "2":
                my_agenda.display_contact()
            elif option == "3":
                name = input("Ingrese el nombre del contacto a buscar: ")
                my_agenda.search_contact(name)
            elif option == "4":
                name = input("Ingrese el nombre del contacto a editar: ")
                new_phone = input("Ingrese el nuevo teléfono: ")
                new_email = input("Ingrese el nuevo correo electrónico: ")
                my_agenda.update_contact(name, new_phone, new_email)
            elif option == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")