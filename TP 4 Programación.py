'''
1) Crea un bucle while con las siguientes características:

• El valor inicial de la variable x será 0.
• El valor de incremento será 1.
• La condición de salida del bucle será mayor o igual a 30.
• La ejecución debe interrumpirse cuando x sea igual a 15.
• Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 
'El valor del bucle es: ' + x.
• Debes omitir las ejecuciones con el valor de x en 4, 6 y 10.
• En cada salto de ejecución, debes mostrar los valores saltados con este mensaje: '
Se omitió el valor ' + x + ' de x'.
• Cuando la ejecución del bucle se interrumpa, debes mostrar un mensaje indicándolo: 
'La ejecución del bucle se interrumpió cuando x era ' + x.
'''

x = 0

while x <= 30:
    x = x + 1
    
    if x == 15:
        print(f"La ejecución del bucle se interrumpió cuando x era: {x}")
        break
    elif x == 4 or x == 6 or x == 10:
        print(f"Se omitio el valor: {x}")
    else:
        print(f"El valor del bucle es: {x}")

#2) Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
# Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

while True:
    line = input("Ingrese una línea (o presione Enter para finalizar): ")
    
    if line == "":
        break
    else:
        print(line.upper())

print("Fin de la entrada de líneas.")

'''
3) Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350
'''
longbook_sum = 0

while True:
    longbook = input("Ingresa [D] si queres depositar tu dinero y [R] si queres retirar dinero: ")
    
    if longbook == "":
        break
    elif longbook[0] == "D":
        aux = int(longbook[1:])
        longbook_sum = longbook_sum + aux
    elif longbook[0] == "R":
        aux = int(longbook[1:])
        longbook_sum = longbook_sum - aux

print(f"El saldo final de su bitacora es {longbook_sum}")

#4) Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente 
# dos divisores distintos: él mismo y el 1.

prime = 0

while True:
    number = int(input("Ingrese un numero, si quiere terminar con la ejecucion ingrese [0]: "))
    if number == 0:
        break
    elif number <= 1:
        continue
    elif number <= 3:
        prime = prime + 1
    elif number % 2 == 0 or number % 3 == 0:
        continue
    else:
        prime = prime + 1

print(f"La cantidad de numeros primos es: {prime}")

#5) Escribir un programa que permita al usuario ingresar dos años y 
# luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y 
# no debe ser divisible por 100, excepto que también sea divisible por 400.

year1 = int(input("Ingrese el año de inicio del programa: "))
year2 = int(input("Ingrese el año de finalización del programa: "))
i = year1

while True:
    i = i + 1
    if i == (year2):
        break
    elif i % 10 and (i % 4 == 0 and (i % 100 == 0 and i % 400 == 0)):
        print(f"El año {i} es bsisesto")

#6) Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
# Utiliza la declaración continue para omitir los números impares.

for i in range(20):
    if i % 2 != 0:
        continue
    print(i)

#7) Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
# Cuando encuentres el número, usa break para salir del bucle.

number_list = [12, 45, 23, 44, 60]

for i in number_list:
    if i == 45:
        break

print("Numero encontrado!!!")

#8) Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
# Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", 
# utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

while True:
    option = int(input("Ingrese uno de los siguientes numeros: [1, 2, 3] o para salir: [0]: "))
    if option == 1:
        print("Usted ha seleccionado la opcion n°1")
        continue
    elif option == 2:
        print("Usted ha seleccionado la opcion n°2")
        continue
    elif option == 3:
        print("Usted ha seleccionado la opcion n°3")
        continue
    elif option == 0:
        print("Salir!")
        break

