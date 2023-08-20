#1) Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input(f'Ingrese la base del rectangulo'))
altura = float(input(f'Ingrese la alutra del rectangulo'))

perimetro = 2 * base + 2 * altura
area = base * altura
print(f'El perimetro del rectangulo es: {perimetro} y el area es: {area}')

#2) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

lado1 = float(input(f'Ingrese el lado 1 del triangulo: '))
lado2 = float(input(f'Ingrese el lado 2 del triangulo: '))

hipotenusa = (lado1**2 + lado2**2)**0.5
print(f'La Hipotenusa del triangulo es: {hipotenusa}')

#3) Dados dos números, mostrar la suma, resta, división y multiplicación de ambos

num1 = float(input(f'Ingrese el numero 1: '))
num2 = float(input(f'Ingrese el numero 2: '))

suma = num1 + num2
resta = num1 - num2
div = num1 / num2
mult = num1 * num2

print(f'El resultado de la suma es: {suma}, de la resta es: {resta}')
print(f', de la multiplicacion es: {mult}, de la division es: {div}')

#4) Escribir un programa que convierta un valor dado en grados Fahrenheit 
# a grados Celsius. Recordar que la fórmula para la conversión es:

gradof = float(input(f'Ingrese los grados en Fahrenheit: '))
gradoc = (gradof - 32) * 5 / 9

print(f'Los grados ingresados en Fahrenheit {gradof}F, pasado a Celsius es: {gradoc}°')

#5)    5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
#    a) A = input(nombre, “¿Cuál es tu canción favorita?”)

A = (input(f'¿Cuál es tu canción favorita?'))

#    b) precio = input(“Precio: “)
#total = precio + (precio * 0.1)

precio = float(input('Precio: '))
total = precio + (precio * 0.1)

#    c) edad = int(input(“Edad: “))
#print(tu edad es, edad)

edad = int(input('Edad: '))
print(f'tu edad es, {edad}')

#    d) edad = int(input(“Edad: “))
#print(“Veamos si tu edad es 18…”, edad=18)

edad = int(input(f'Edad: '))
print(f'Veamos si tu edad es 18…, {edad == 18}')

#6) Calcular la media de tres números pedidos por teclado.

num1 = float(input(f'Ingrese el numero 1: '))
num2 = float(input(f'Ingrese el numero 2: '))
num3 = float(input(f'Ingrese el numero 3: '))

promedio = 3 / (num1 + num2 + num3)
print(f'El promedio de los 3 numeros anteriormente ingresados es: {promedio}')

#7) Realiza un programa que reciba una cantidad de minutos y muestre por pantalla 
# a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

num1 = int(input(f'Ingrese una cantidad de minutos: '))

horas = num1 / 60
print(f'LOs minutos anteriormente ingresados son iguales a: {horas} hrs')

#8) Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
# por las tres ventas que realiza en el mes 
# y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldobase = float(input("Ingrese el sueldo base del vendedor: "))

venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

totalcomisiones = comision1 + comision2 + comision3
totalrecibido = sueldobase + totalcomisiones
print(f"Total de comisiones: {totalcomisiones}")
print(f"Total recibido en el mes: {totalrecibido}")

#9) Una tienda ofrece un descuento del 15% sobre el total de la compra 
# y un cliente desea saber cuanto deberá pagar finalmente por su compra.

cantidad_articulos = int(input("Ingrese la cantidad de artículos en su compra: "))
totalcompra = 0

for i in range(cantidad_articulos):
    precio_articulo = float(input(f"Ingrese el precio del artículo {i+1}: "))
    totalcompra += precio_articulo

descuento = totalcompra * 0.15
montofinal = totalcompra - descuento

print(f"Total de la compra antes del descuento: {totalcompra}")
print(f"Descuento aplicado: {descuento}")
print(f"Monto final a pagar: {montofinal}")

#10)    10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#   •     55% del promedio de sus tres calificaciones parciales.
#   •     30% de la calificación del examen final.
#   •     15% de la calificación de un trabajo final.

totalparciales = 0

for i in range(3):
    notaparciales = float(input(f"Ingrese la nota del parcial N°{i+1}: "))
    totalparciales += notaparciales

promedioparciales = totalparciales / 3

examenf = float(input("Ingrese la nota del Examen Final "))
trabajof = float(input("Ingrese la nota del Trabajo Final "))

notafinal = (promedioparciales * 0.55) + (examenf * 0.30) + (trabajof * 0.15)

print(f"Nota final de la materia Algoritmos: {notafinal}")

#11)Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

diferencia = abs(num1 - num2)
print(f"La distancia entre los números es: {diferencia}")

#12)Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica

numero = float(input("Ingrese un numero: "))

raiz2 = numero ** (1/2)
raiz3 = numero ** (1/3)
print(f"La raiz cuadrada de {numero} es: {raiz2} y su raiz cubica es: {raiz3}")

#13)Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
# Ejemplo, si se introduce 23 que muestre 32.

numero = int(input("Ingrese un número de dos cifras: "))

cifra1 = numero // 10
cifra2 = numero % 10   

numero_invertido = cifra2 * 10 + cifra1
print(f"El número invertido es: {numero_invertido}")

#14)Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables y 
# muestre cuanto valen al final las dos variables.

A = float(input("Ingrese el valor de la variable A: "))
B = float(input("Ingrese el valor de la variable B: "))

aux = A
A = B
B = aux

print(f"El valor final de la variable A es: {A}")
print(f"El valor final de la variable B es: {B}")

#15)Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

HH = int(input("Ingrese la hora de partida (HH): "))
MM = int(input("Ingrese los minutos de partida (MM): "))
SS = int(input("Ingrese los segundos de partida (SS): "))
T = int(input("Ingrese el tiempo de viaje en segundos (T): "))

hora_en_segundos = HH * 3600 + MM * 60 + SS

hora_llegada_en_segundos = hora_en_segundos + T

HH_llegada = hora_llegada_en_segundos // 3600
MM_llegada = (hora_llegada_en_segundos % 3600) // 60
SS_llegada = hora_llegada_en_segundos % 60
print(f"Hora de llegada: {HH_llegada}:{MM_llegada:02d}:{SS_llegada:02d}")

#16) Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[0] + apellido1[0] + apellido2[0]
print("Las iniciales son:", iniciales)

#17) Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable 
# llamada usuario. A continuación mostrar por pantalla: 
# “Ahora estás en la matrix, [nombre del usuario]”.

usuario = input("Ingrese su nombre: ")
print(f'Ahora estás en la matrix, {usuario}')

#18) Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. 
# A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. 
# Imprimir en pantalla el monto final a pagar.

costoparcial = float(input("Ingrese el costo de la cena: "))

costototal = (costoparcial * 0.062) + (costoparcial * 0.10) + costoparcial
print(f'El monto final a pagar es de: {costototal:.2f}')

#19) Solicitar al usuario que ingrese el día, mes y año de su nacimiento y 
# almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). 
# Finalmente, mostrar la fecha en formato dd/mm/aaaa.

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

fecha_nacimiento = f"{dia:02d}/{mes:02d}/{anio}"
print("Su fecha de nacimiento es:", fecha_nacimiento)

#20) Hacer otra versión del programa, 
# pero esta vez almacenado todo en una única variable con formato DDMMAAA.

fecha_completa = input("Ingrese su fecha de nacimiento (DDMMAAAA): ")

dia = int(fecha_completa[0:2])
mes = int(fecha_completa[2:4])
anio = int(fecha_completa[4:])

fecha_nacimiento = f"{dia:02d}/{mes:02d}/{anio}"
print("Su fecha de nacimiento es:", fecha_nacimiento)

#21)     21. Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, 
# para saber cuántos tanques de combustible consumirá el viaje entero.
#Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, 
# qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

km_por_litro = float(input("Ingrese los kilómetros por litro de su moto: "))
capacidad_tanque = float(input("Ingrese la capacidad del tanque en litros: "))
kilometros_totales = float(input("Ingrese la cantidad total de kilómetros del viaje: "))

litros_necesarios = kilometros_totales / km_por_litro
tanques_necesarios = litros_necesarios / capacidad_tanque
print(f"Para recorrer {kilometros_totales:.2f} km, necesitarán {tanques_necesarios:.2f} tanques de combustible.")
