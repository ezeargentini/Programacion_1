#Ejercicio 1
import Funciones
list_passengers = [('Jeronimo Cortez', 44820614, 'Mendoza'), #Tupla con nombre, dni, destino del pasajero
                    ('Manuel Juarez', 12345678, 'San Juan')]
list_destinations = [('Mendoza', 'Argentina'), ('Reñaca', 'Chile'), #Tupla con destino y su pais
                        ('Buenos Aires', 'Argentina'), ('San Juan','Argentina')]
while True:
    print(f'--- Menu de opciones ---\n'
            '1.Agregar un pasajero a la lista\n'
            '2.Agregar un destino a la lista\n'
            '3.Ver ciudad de destino de un pasajero\n'
            '4.Mostrar la cantidad de pasajeros que viajan a una ciudad\n'
            '5.Ver pais de destino de un pasajero\n'
            '6.Mostrar la cantidad de pasajeros que viajan a un pais\n'
            '7.Salir del programa')
    option = int(input("Ingrese una opcion: "))
    if option >= 1 and option <= 7:
        if option == 1:
            list_passengers = Funciones.add_passengers(list_passengers)
        elif option == 2:
            list_destinations = Funciones.add_destinations(list_destinations)
        elif option == 3:
            id = int(input("Ingrese el dni del pasajero: "))
            destination_passenger = Funciones.destination_passenger(id, list_passengers)
            if destination_passenger == False:
                print("Ingreso un dni incorrecto")
            elif destination_passenger != False:
                print(f'El destino del pasajero es {destination_passenger}')    
        elif option == 4:
            destination = str(input("Ingrese la ciudad del destino: ")) 
            cant_passenger = Funciones.cant_passenger_destination(destination, list_passengers)
            print(f'La cantidad de pasajeros que viajan al destino {destination} es {cant_passenger}')
        elif option == 5:
            id_number = int(input("Ingrese el dni del pasajero: "))
            country_passenger = Funciones.country_destination_passenger(id_number, list_passengers, list_destinations)
            print(f'El pais de destino del pasajero es: {country_passenger}')
        elif option == 6:
            country = str(input("Ingrese un pais: "))
            cant = Funciones.cant_country_passenger(country,list_passengers,list_destinations)
            print(f'Al destino viajan {cant} pasajeros')
        elif option == 7:
            break    

#Ejercicio 2
sales = (('Jeronimo Cortez', 4, 12330, 'Lugones 277'), 
            ('Manuel Juarez', 5, 14550, 'Olascoaga 49'),
            ('Jeronimo Cortez', 8, 16330, 'Lugones 277'))   
unique_address = Funciones.get_unique_address(sales)
print("Las direcciones para facturar son")
for i in unique_address:
    print(i)

#Ejercicio 3
registred_members = { 1 : {"nombre":"Amanda nuñez", "Fecha_ingreso":"17/03/2009","Cuota_al_dia": True},
                        2 : {"nombre":"Bárbara Molina", "Fecha_ingreso":"17/03/2009","Cuota_al_dia":True},
                        3 : {"nombre":"Lautaro Campos", "Fecha_ingreso":"17/03/2009","Cuota_al_dia":False}
} 
while True:
    print("--- Menú ---")
    print("1. Informar cantidad de socios")
    print("2. Registrar pago de cuotas")
    print("3. Modificar fecha de ingreso")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")
    option = int(input("Ingrese una opcion: "))
    if option == 1:
        print(f'La cantidad de socios es: {Funciones.cant_members(registred_members)}')
    elif option == 2:
        number_member = int(input("Ingrese el numero de socios: "))
        Funciones.dues_payment(number_member, registred_members)
    elif option == 3:
        number_member = int(input("Ingrese el numero de socios: "))
        Funciones.modify_admission_date(number_member, registred_members)
    elif option == 4:
        name = str(input("Ingrese el nombre del socio: "))
        Funciones.delete_member(name, registred_members)
    elif option == 5:
        Funciones.print_list(registred_members) 
    elif option == 6:
        print("Salio del programa")
        break


     


