#1) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")

for i in range (10):
    print(word)

#2) Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))

for i in range(age):
    print(f"Usted ha cumplido {i} año/s")

#3) Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas

number = int(input("Ingrese un numero: "))
list_odd = []

if number > 0:
    for i in range(number):
        if i % 2 == 0:
            list_odd.append(i)

print(f"Todos los números impares desde 1 hasta {number} son: ")
print(list_odd)

#4) Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("Ingrese un numero: "))
list_inverted = []

if number <= 0:
    print("Error numero invalido")
else: 
    for i in range(number + 1):
        num_inverted = number - i
        list_inverted.append(num_inverted)

if number > 0:
    print(f"La cuenta regresiva es: ... ")
    print(list_inverted)

#5) Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión cada año que dura la inversión.

investment = float(input("Ingrese una cantidad de dinero a invertir: "))
interest = float(input("Ingrese el interes anual: ")) / 100
years = int(input("Ingrese la cantidad de años que va a durar la inversion: "))

annual_profit = investment

for i in range(years):
    annual_profit = annual_profit + (annual_profit * interest)
    print(f"La gananacia en el año {i + 1} es {annual_profit}")

#6) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo, de altura el número introducido.

number = int(input("Por favor, introduce un número entero: "))

if number > 0:
    for i in range(1, number + 1):
        print('*' * i)
else:
    print("Por favor, introduce un número entero positivo.")

#7) Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1, 10):
    print(f"La tabla del {i} es: ")
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")

#8) Escribir un programa que pida al usuario un número entero y muestre por pantalla 
# un triángulo rectángulo como el de más abajo.

number = int(input('Ingrese un numero: '))
for i in range(1, number + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()   

#9) Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = "contraseña"
password2 = input("Introduzca la contraseña: ")

while password != password2:
    password2 = input("Contraseña Incorrecta... Introduzca ptra vez la contraseña: ")

print("Felicitaciones cotraseña correcta")

#10) Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.

number = int(input("Ingresa el numero"))

if number > 0:
    print()

#11) Escribir un programa que pida al usuario una palabra y luego muestre por 
# pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Ingrese una palabra: ")

for i in reversed(word):
    print(i)

#12) Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Ingrese una frase: ").lower()
letter = input("Ingresa una letra para buscarla en la frase anteriormente ingresada: ").lower()
counter = 0

for i in phrase:
    if i == letter:
        counter = counter + 1

print(f"La letra {letter} se encuentra {counter} vez/veces en la frase")

#13) Escribir un programa que muestre el eco de todo lo que 
# el usuario introduzca hasta que el usuario escriba “salir” que terminará.

phrase = ""

while phrase != "salir":
    phrase = input("Ingrese una frase para ver su eco: ").lower()
    if phrase != "salir":
        print(f"{phrase}... ")

print("Nos vemos")

#14) Escriba un programa que pida dos números enteros 
# y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

for i in range(number1 + 1, number2):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

#15) Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

number = int(input("Ingrese un numero entero: "))

for i in range(number):
    if i != 0:
        if number % i == 0:
            print(f"{i} si es divisor de {number}")

#16) Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números y escriba cuántos negativos ha introducido.

number = int(input("Ingrese la cantidad de numeros que va a ingresar: "))
negative = 0

for i in range(number):
    num = int(input(f"Ingrese el numero N°{i + 1}: "))
    if num < 0:
        negative = negative + 1

print(f"Hay {negative} numeros negativos en los numeros ingresados")

#17) Solicitar al usuario que ingrese una frase y 
# luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("Ingrese una frase para ver que vocales contiene: ").lower()

vowels = []

for letter in phrase:
    if letter.lower() in 'aeiou' and letter.lower() not in vowels:
        vowels.append(letter.lower())

print("Vocales en la frase:")
for vowel in vowels:
    print(f"Las vocales que aparecen son: {vowels}")

#18) Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
# cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

a = 0
b = 1

print("Los primeros 10 números de la sucesión de Fibonacci son:")
print(f"f(0) = {a}")  
print(f"f(1) = {b}")  

for i in range(8):
    
    c = a + b
    a = b
    b = c

    print(f"f({i + 2}) = {c}")

#19) Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
# que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará 
# una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
# El programa deberá comprobar que las cantidades ingresadas sean positivas.

objetive = int(input("Ingrese el objetivo de dinero a ahorrar: "))
addition = 0

while addition < objetive:
    amount = int(input("Ingrese un monto"))
    if addition >= 0:
        addition = addition + amount
        print(f"Usted lleva ahorrado: {addition}$")
    else:
        print("Error valor negativo")

print("Felicidades objetivo alcanzado!!!")


#20) Leer números enteros de teclado, 
# hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

number = 1
addition = 0

while number != 0:
    number = int(input("Ingrese un numero: "))
    addition = addition + number

print(f"La suma de todos los numeros ingresados es: {addition}")

#21) Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
# Informar cuál fue el mayor número ingresado.

number = 1
bigger = 1

while number != 0:
    number = int(input("Ingrese un numero: "))
    if number > bigger:
        bigger = number

print(f"El mayor numero ingresado es: {bigger}")

#22) Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
# imprimir la suma de los dígitos que lo componen. La condición de corte es que se 
# ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por 
# el usuario fueron números pares.

number = 0

while number != -1:
    number = int(input("Ingrese un numero entero positivo: "))
    number_str = str(number)
    if number >= 0:
        aux = 0
        for i in number_str:
            aux = aux + int(i)
        print(f'La suma de las cifras del numero {number} es {aux}')

#23) Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0.

purchase = 1
purchase_list = []

while purchase != 0:
    purchase = int(input("Ingrese el monto de su compra, para finalizar ingrese 0: "))
    purchase_list.append(purchase)

print(f'Los montos de las compras del cliente son: {purchase_list}')  

#24) Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

purchase = 1
purchase_list = []

while purchase != 0:
    purchase = int(input("Ingrese el monto de su compra, para finalizar ingrese 0: "))
    if purchase > 0:
        purchase_list.append(purchase)    
    else:
        print("No puede ingresar montos negativos")

total = sum(purchase_list)
if total > 1000:
    total = total - (total * 0.10)

print(f'Los montos de las compras del cliente son: {purchase_list}, el total es ${total}') 

#25) Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos 
# los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

number = int(input("ingrese un numero entero positivo: "))
factorial = 1

if number == 0:
    factorial = 1
elif number > 0:
    for i in range(1, number + 1):    
        factorial = factorial * i

print(f'El factorial de {number} es {factorial}')