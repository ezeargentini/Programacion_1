"""
Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje *considerando la posición de cada una en el alfabeto* una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
"""

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

corrimiento = int(input("Ingrese la cantidad de lugares a correr: "))
mensaje_jefe = input("Ingrese el mensaje del jefe: ")

for _ in range(5):
    mensaje_oficial = input("Ingrese el mensaje del oficial: ")
    mensaje_encriptado = ""
    for letra in mensaje_oficial:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.upper()
            indice = (alfabeto.index(letra) + corrimiento) % 26
            letra_encriptada = alfabeto[indice]
            if not mayuscula:
                letra_encriptada = letra_encriptada.lower()
            mensaje_encriptado += letra_encriptada
        else:
            mensaje_encriptado += letra
    print("Mensaje encriptado:", mensaje_encriptado)

"""
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
"""

total_digitos_pares = 0
total_digitos_impares = 0

while True:
    numero = int(input("Ingrese un número (ingrese 0 para salir): "))
    
    if numero == 0:
        break
    
    digitos_pares = 0
    digitos_impares = 0
    
    num_temp = numero
    while num_temp > 0:
        digito = num_temp % 10
        if digito % 2 == 0:
            digitos_pares += 1
        else:
            digitos_impares += 1
        num_temp //= 10
    
    total_digitos_pares += digitos_pares
    total_digitos_impares += digitos_impares
    
    print(f"El número {numero} tiene {digitos_pares} dígitos pares y {digitos_impares} dígitos impares.")

print("Resumen:")
print(f"Total de dígitos pares leídos: {total_digitos_pares}")
print(f"Total de dígitos impares leídos: {total_digitos_impares}")

