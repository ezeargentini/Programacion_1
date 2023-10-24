import Funciones
#Ejercicio 1
number = -1
while number <= 0:
    number = int(input("Ingrese un numero entero positivo: "))
    if number <= 0:
        print("El numero no es entero positivo")
    else:
        print(f'La cantidad de digitos que tiene el numero es {Funciones.add_digits_recursion(number)}') 

#Ejercicio 2
base = int(input("Ingrese la base de la potencia: "))
exponent = int(input("Ingrese el exponente de la potencia: ")) 
print(f'{base} es potencia de {exponent}: {Funciones.is_power_of(base,exponent)}')

#Ejercicio 3
phrase = str(input("Ingrese una frase: "))
fragment = str(input("Ingrese que fragmento desea buscar en la frase: "))
positions  = Funciones.find_position(phrase,fragment)
if len(positions) == 0:
    print("El fragmento no esta en la frase")
else:
    print(f'El fragmento {fragment} esta en las posiciones {Funciones.find_position(phrase, fragment)} de la frase {phrase}')

#Ejercicio 4



