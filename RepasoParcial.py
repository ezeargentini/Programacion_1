#Vamos crear un programa que simule un juego de adivinanzas, va a generarse un 
#numero aleatorio entre 1 y 100, si el usuario no adivina el le daremos hasta 3
#pistas, al finalizar se le mostrara cuantos intentos ingreso

import random

number = random.randint(1,100) #Esta funcion nos genera un numero aleatorio entre 1 y 100
print("Bienvenidos al juego de adivinanza!!!\n"
        "El numero esta entre 1 y 100\n"
        "Tiene 10 intentos\n")
tries = 0 #Inicilizamos el contador de intento
list_number = [] #Inicilizamos una lista para los numeros que ingresa el usuario 

while True:
    
    cont = 0
    number_user =int(input("Ingrese el numero: "))
    list_number.append(number_user)   
    tries += 1
    
    for i in list_number:
        if i == number_user:
            cont += 1
            if cont >= 2:
                tries -= 1
                print("Ya ingreso el numero")
                break
    if number != number_user:
        if number < 50 and tries == 3:
            print("El numero es menor a 50")
        elif number > 50 and tries == 3 :
            print("EL numero es mayor a 50")
        elif tries == 6:
            if number < 10:
                print(f'El numero esta entre 1 y {number + 10}')
            elif number > 90:
                print(f'EL numero esta entre {number - 10} y 100')
            else:    
                print(f'El numero esta entre {number - 10} y {number + 10}')       
        elif tries == 9:
            print(f'El triple del numero sumado 10 es {(number * 3) + 10}') 
        elif tries == 10:
            print(f'Se le termino los intentos el numero era {number} :(')   
            break        
    elif number == number_user:
        print(f'Felicitaciones adivino el numero {number}!!! en {tries} intentos')
        break  
    
    print("Ingreso un numero incorrecto")
