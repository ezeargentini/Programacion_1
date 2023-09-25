import Funciones
sumation_digit = 0
sumation = 0
num = int(input("Ingrese un numero: "))
while num != 0:
    sumation = sumation + num
    sumation_digit += Funciones.add_digits(num)
    print(f'Suma: {Funciones.add_digits(num)}')
    num = int(input("Ingrese un numero: "))
print(f'La suma de los digitos de todos los numeros ingresados es {sumation_digit}')
print(f'La sumatorio de los numeros ingresados es {sumation}')

#Ejercicio 1
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro numero: "))

print(Funciones.most(x-3, Funciones.least(x+2, y-5)))
    
