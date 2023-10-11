import Funciones

#1) Escribir una función que, dado un número de DNI, 
# retorne True si el número es válido y False si no lo es. 
#Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

number_DNI = int(input("Ingresa tu DNI: "))
bool = Funciones.check_ID(number_DNI)
print(bool)

#2) Escribir una función que, dado un string, 
# retorne la longitud de la última palabra. 
#Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o 
# al final del string pasado por parámetro.

phrase = input("Ingresar una frase o palabra: ")
result = Funciones.last_word(phrase)
print(result)

#3) Escribir un programa que permita al usuario obtener 
# un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, 
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre apellido. 
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. 
# Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, 
# el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único, 
# el cual estará formado por: el primer nombre, la cantidad de letras del apellido 
# y los 3 primeros dígitos de su DNI. Ejemplo:
# 
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254

print("Registro de socios")
while(True):
    name_complete, dni = Funciones.socios_registry()
    if name_complete == False:
        break
    else:
        print(f'El id del socio {name_complete} es {Funciones.generator_id(name_complete, dni)}')

print("Salio del programa")

#4) Crea un programa que pida dos número enteros al usuario y 
# diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si 
# el primero es múltiplo del segundo.

number_one = int(input("Ingrese un numero: "))
number_two = int(input("Ingrese otro numero: "))
multiple = Funciones.is_multiple(number_one, number_two)
if multiple == True:
    print(f'{number_one} es multiplo de {number_two}')
else:
    print(f'Los numeros ingresados no son multiplos')   

#5) Crear una función que calcule la temperatura media 
# de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, 
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
# El programa pedirá el número de días que se van a introducir.

day = int(input("Ingrese la cantidad de dias que desea saber la tmperatura: "))
for i in range(1, day + 1):
    temperature_min = float(input(f'Ingrese la temperatura minima del dia {i}: '))
    temperature_max = float(input(f'Ingrese la temperatura maxima del dia {i}: '))
    print(f'La temperatura media del dia {i} es {Funciones.average_temperature(temperature_min, temperature_max)}')

#6) Crea una función que reciba como parámetro un texto 
# y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función.

text = str(input("Ingrese un texto o frase: "))
print(f'El nuevo texto es {Funciones.converted_text(text)}')    

#7) Crea una función que recibe una lista con valores numéricos 
# y devuelve el valor máximo y el mínimo. 
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, 
# utilizando la función anterior.

number_list = []
while True:
    number = int(input("Ingrese un numero: "))
    number_list.append(number)
    finish = str(input("Ingrese una S para salir: "))
    if finish == 'S':
        break
number_min, number_max = Funciones.min_and_max_number(number_list)
print(f'El numero minimo de la lista es {number_min} y el numero maximo es {number_max}')

#8) Diseñar una función que calcule el área y 
# el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que 
# lea el radio de una circunferencia y muestre su área y perímetro.

radius = int(input("Ingrese el radio de la circunferencia: "))
area, perimeter = Funciones.area_and_perimeter(radius)
print(f'El area de la circunferencia es {area} y el perimetro de la circunferencia es {perimeter}')

#9)  Crear una subrutina llamada “login”, que recibe un nombre 
# de usuario y una contraseña y te devuelve Verdadero si 
# el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
# Además recibe el número de intentos que se ha intentado hacer login y 
# si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y 
# una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

tries = 0
while tries < 3:
    user = str(input("Ingrese el nombre de usuario: "))
    password = str(input("Ingrese la contraseña: "))
    login = Funciones.check_login(user,password)
    if login == False:
        print("Usuario o contraseña incorrectos")
        tries += 1
    elif login == True:
        print("Ingreso exitosamente")
        break
if tries >= 3:
    print("El ingreso no se pudo realizar alcanzo los 3 intentos")  

#10)  Escribir una función que aplique un descuento a un precio. 
# Esta función tiene que recibir un diccionario con los precios 
# y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  
# y devolver el precio final de la compra.

cart = {
    "producto1": 100,
    "producto2": 50,
    "producto3": 200
}
discount = {
    "producto1": 10,
    "producto3": 15
}

final_price = Funciones.aplicar_descuento(cart, discount)
print("Precio final con descuento:", final_price)

#11. Escribir una función que reciba otra función y una lista, 
# y devuelva otra lista con el resultado de aplicar la función dada a cada uno 
# de los elementos de la lista.

number = [1, 2, 3, 4, 5]
result = Funciones.aplicar_funcion_a_lista(Funciones.sumar_uno, number)

print("Lista original:", number)
print("Lista con la función aplicada:", result)

#12. Escribir una función que reciba una frase y devuelva un diccionario 
# con las palabras que contiene y su longitud.

phrase = input("Ingrese una frase")
result = Funciones.obtener_longitudes_palabras(phrase)
print("Diccionario de palabras y sus longitudes:", result)

#13. Escribir una función que calcule el módulo de un vector.

vector_size = int(input("Ingrese el tamaño del vector: "))
vector = []

for _ in range(vector_size):
    element = int(input("Ingrese un elemento para el vector: ")) 
    vector.append(element)

module = Funciones.calcular_modulo_vector(vector)
print("El módulo del vector es:", module)

#14. Requerir al usuario que ingrese un número entero e informar 
# si es primo o no, utilizando una función booleana que lo decida.

number = int(input("Ingrese un numero entero: "))
is_prime = Funciones.is_prime(number)
if is_prime == True:
    print(f'El numero {number} es primo')
else:
    print(f'El numero {number} no es primo')

#15. Escribir un programa que pida números al usuario, motrar el factorial de cada uno 
# y, al finalizar, la cantidad total de números leídos en total. 
# Utilizar una o más funciones, según sea necesario.

while True:
    number = int(input("Ingrese un numero entero(Para salir ingrese 0: "))
    if number == 0:
        print(f'El factorial de 0 es 1')
        break
    elif number > 0:
        print(f'El factorial de {number} es {Funciones.factorial(number)}')
    elif number < 0:
        print("No se puede calcular numero negativos")    

#16. Solicitar al usuario un número entero y luego un dígito. 
# Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

number = int(input("Ingrese un numero entero: "))
digit = int(input("Ingrese un digito: "))
print(f'La frecuencia del digito {digit} en el numero es: {Funciones.calculate_frecuency(number,digit)}')        

#17. Solicitar al usuario el ingreso de números primos. 
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito 
# e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

older = 0
while True:
    number = int(input("Ingrese un numero primo: "))
    is_prime = Funciones.is_prime(number)
    if number > older:
        older = number
    if is_prime == True:
        sum_digits = Funciones.add_digits(number)
        print(f'La suma de los digitos del numero {number} es {sum_digits}')
        digit = int(input("Ingrese un digito: "))
        frequency_digit = Funciones.calculate_frequency(number,digit)
        print(f'El digito {digit} esta {frequency_digit} veces en el numero')
    elif is_prime == False or number < 0:
        break

print(f'El mayor numero ingresado fue {older} y su factorial {Funciones.factorial(number)}')

