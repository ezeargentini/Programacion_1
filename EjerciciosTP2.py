#1) Crear un programa que reciba el número de años que tiene nuestra 
#computadora y muestre en la consola que 
#el computador es nuevo si es menor o igual a 2 años y que el 
#computador es viejo si es mayor a 2 años.

aniosc = int(input("Ingrese el numero de años que tiene la computadora"))

if aniosc >= 0 and aniosc < 2:
    print("La computadora es nueva")
elif aniosc >= 0 and aniosc > 2:
    print("La computadora es vieja")

#2) Hacer que el programa anterior muestre un mensaje de error si 
#el usuario digita un número negativo.

aniosc = int(input("Ingrese el numero de años que tiene la computadora"))

if aniosc >= 0 and aniosc < 2:
    print("La computadora es nueva")
elif aniosc >= 0 and aniosc > 2:
    print("La computadora es vieja")
elif aniosc < 0:
    print("FEcha incorrecta")

#3) Solicitar al usuario que ingrese los nombres de dos personas, 
#los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ 
#si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1 = input("Ingrese el primer nombre")
nombre2 = input("Ingrese el segundo nombre")

if nombre1[0] == nombre2[0]:
    print("coincidencia")
else:
    print("No hay coincidencia")

#4) Crear un programa que permita al usuario elegir un candidato por el cual votar. 
#Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, 
#candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘
#Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
#indicar ‘Opción errónea.’

voto = input("Ingrese la letra del partido a votar A, B o C")
voto = voto.lower()

if voto == 'a':
    print("Usted ha votado por el partido rojo")
elif voto == 'b':
    print("Usted ha votado por el partido verde")
elif voto == 'c':
    print("Usted ha votado por el partido azul")
else:
    print("Opcion erronea")

#5) Escribir un programa que solicite al usuario una letra, 
#si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. 
#Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra = input("Ingrese una letra")
letra = letra.lower()

if len(letra) == 1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Es vocal")
else:
    print("No se puede procesar el dato")

#6) Hacer un programa que permita saber si un año es bisiesto. 
#Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
#excepto que también sea divisible por 400.

aniob = int(input("Ingrese el año"))

if (aniob % 4 == 0 and aniob % 100 != 0) or aniob % 400 == 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

#7) Escribí un programa para solicitar al usuario tres números 
#y mostrar en pantalla al menor de los tres

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

menor = num1

if menor > num2:
    menor = num2
elif menor > num3:
    menor = num3

print(f"El menor de los numeros es: {menor}")

#8) Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
#Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla 
#“Usuario y contraseña correctos. Puede ingresar a Camelot”. 
#Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

usuario = input("Ingrese el nombre de usuario")
contrasenia = input("Ingrese la contraseña")

if usuario == 'Gwenevere' and contrasenia == 'excalibur':
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#9) Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A está formado por las mujeres con un nombre anterior a la M 
#y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
#pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (F/M): ")

if (sexo.upper() == 'F' and nombre.lower() < 'm') or (sexo.upper() == 'M' and nombre.lower() > 'n'):
    print('Usted pertenece al grupo A')
else:
    print('Usted pertenece al grupo B')

#10) Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
#y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
#El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
#Si el cliente es menor de 4 años puede entrar gratis, 
#si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000

edad = int(input("Ingrese su edad"))

if edad < 4:
    print("Usted entra gratis")
elif edad > 4 and edad < 18:
    print("Usted debera paga $500")
elif edad > 18:
    print("Usted debera paga $1000")
else:
    print("Edad Incorrecta")

#11) La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#    • Ingredientes vegetarianos: Pimiento y tofu.
#    • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
#en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
#Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas 
#las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
#todos los ingredientes que lleva

pizzasn = input("Ingrese si quiere una pizza vegetariana o no [S/n]")

if pizzasn == "S":
    ingrediente = input("Elija el ingrdiente a agregar ademas de la muzzarella y el tomate, [1](Pimiento o Tofu)")
    print(f"La pizza es vegetariana y los ingredientes son: muzarella, tomate y {ingrediente}")
elif pizzasn == "n":
    ingrediente = input("Elija el ingrdiente a agregar ademas de la muzzarella y el tomate, [1](Peperoni, Jamon o Salmon)")
    print(f"La pizza es vegetariana y los ingredientes son: muzarella, tomate y {ingrediente}")
else:
    print("Dato Incorrecto")

#12) Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años 
#han pasado desde ese año o cuántos años faltan para llegar a ese año.

anioa = int(input("Ingrese el año actual: "))
anioc = int(input("Ingrese un año cualquiera: "))

if anioa > anioc:
    aniof = anioa - anioc
    print(f"Faltan {aniof} años para el año {anioa}")
elif anioa < anioc:
    aniof = anioc - anioa
    print(f"Faltan {aniof} años para el año {anioc}")
else:
    print("Estas en ese año")

#13) Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
#Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

menor = num1
mayor = num2

mayor = max(num1, num2)
menor = min(num1, num2)

if num1 <= 0 or num2 <= 0:
    print("Por favor ingrese valores positivos y no nulos.")
elif mayor % menor == 0:
    print(f"{mayor} es múltiplo de {menor}.")
else:
    print(f"{mayor} no es múltiplo de {menor}.")

#14) Escriba un programa que pida los coeficientes de una ecuación 
#de primer grado (a x + b = 0) y escriba la solución.
#serecuerda que una ecuación de primer grado puede no tener solución, 
#tener una solución única, o que todos los números sean solución. 
#Se recuerda que la fórmula de las soluciones es 
#x = -b / a

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))

if a == 0 and b == 0:
    print("Todos los números son solución de la ecuación.")
elif a == 0:
    print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}")

#15) Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo 
#o la de un círculo. Si se contesta que se quiere calcular el
#área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces 
#la base y la altura y escribir el área. Si se contesta que se quiere calcular 
#el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces 
#el radio y escribir el área.

calcular = input("Quiere calcular el área de un triángulo[T o t] o la de un círculo[C o c]?")
calcular = calcular.lower()

import math
pi = math.pi

if calcular == "t":
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base * altura) / 2
    print(f"El area del triangulo es de {area:.2f}")
elif calcular == "c":
    radio = float(input("Ingrese el radio del circulo: "))
    area = pi * (radio ** 2)
    print(f"El area del circulo es de {area:.2f}")
else:
    print("Valor incorrecto")

#16) Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#  • Si operación es 1 entonces debemos ver el resultado de a + b
#  • Si operación es 2 entonces debemos ver el resultado de a * b
#  • Si operación es 3 entonces debemos ver el resultado de a - b
#  • Si operación es 4 entonces debemos ver el resultado de a / b

a = float(input("Ingresa el primer valor (a): "))
b = float(input("Ingresa el segundo valor (b): "))

print("Operaciones disponibles:")
print("1. Sumar")
print("2. Multiplicar")
print("3. Restar")
print("4. Dividir")

operacion = int(input("Selecciona una operación (1/2/3/4): "))

if operacion == 1:
    resultado = a + b
elif operacion == 2:
    resultado = a * b
elif operacion == 3:
    resultado = a - b
elif operacion == 4:
    if b != 0:
        resultado = a / b
    else:
        resultado = "Error: No es posible dividir por cero."
else:
    resultado = "Opción no válida"

print(f"El resultado es: {resultado}")

#17) Requerir al usuario que ingrese un día de la semana e imprimir un mensaje 
#si es lunes, otro mensaje diferente si es viernes, 
#otro mensaje diferente si es sábado o domingo. 
#Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana = input("Ingresa un día de la semana: ")

if dia_semana.lower() == "lunes":
    print("Hoy es lunes. ¡Ánimo para empezar la semana!")
elif dia_semana.lower() == "viernes":
    print("¡Ya es viernes! Disfruta del fin de semana.")
elif dia_semana.lower() == "sabado" or dia_semana.lower() == "sábado" or dia_semana.lower() == "domingo":
    print("Es fin de semana. ¡A relajarse!")
else:
    print("Opción no valida")

#18) Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, 
#si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas 
#un 10% más que las horas laborales comunes.

horas_trabajadas = float(input("Ingresa las horas trabajadas en el mes: "))
salario_hora = float(input("Ingresa el salario por hora: "))

if horas_trabajadas < 48:
    print("Usted a trabajado menos de la jornada minima para cobrar su salario")
elif horas_trabajadas >= 48 and horas_trabajadas < 160:
    salario = horas_trabajadas * salario_hora
    print(f"Su salario mensual es de {salario}$")
elif horas_trabajadas > 160:
    horas_extra = horas_trabajadas - 160
    salario = (horas_extra * (salario_hora * 1.10)) + (horas_trabajadas - horas_extra) * salario_hora
    print(f"Su salario mensual es de {salario}$")

#19) Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, 
#existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; 
#de lo contrario no hay descuento.

cant_lapices = int(input("Ingrese la cantidad de lapices que quiere comprar"))

if cant_lapices >= 1000:
    precio = (cant_lapices * 60)
    preciodesc = precio - (precio * 0.07)
    print("Usted ha recibido un descuento por la compra igual o mayor a 1000 lapices!!!")
    print(f"El precio final con el descuente del 7% es {preciodesc}$")
else:
    precio = (cant_lapices * 60)
    print(f"El precio final es {precio}$")

#20) Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara 
#si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

nota1 = float(input("Ingrese la nota N°1: "))
nota2 = float(input("Ingrese la nota N°2: "))
nota3 = float(input("Ingrese la nota N°3: "))
nota4 = float(input("Ingrese la nota N°4: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 6:
    print(f"Usted ha aprobado el curso con un promedio de {promedio}")
else:
    print(f"Usted ha desaprobado el curso con un promedio de {promedio}")





