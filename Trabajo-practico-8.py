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
number = int(input("Ingrese un numero entero: "))
print(f'{number} es par: {Funciones.even(number)}')
print(f'{number} es impar: {Funciones.odd(number)}')

#Ejercicio 5
list_numbers = [1,3,45,1,2]
print(f'El mayor numero de la lista es: {Funciones.most_by_list(list_numbers)}')

#Ejercicio 6
list_numbers = [1,2,3,4,5]
replicate = 2
print(f'La lista con sus valores replicados {replicate} veces es {Funciones.replicate_numbers(list_numbers,replicate)}')

#Ejercicio 7
print(f'El resultado de la sumatoria recursiva es: {Funciones.recursive_summation(2,2)}')

#Ejercicio 8
row = int(input("Ingrese la fila: "))
col = int(input("Ingrese la columna: "))
(f'El valor de la fila {row} y la columna {col} es: {print(Funciones.pascal(row,col))}')

#Ejercicio 9
list_char = ['A','E','D']
length_list = len(list_char)
Funciones.combinations(list_char,length_list)

#Ejercicio 10
paper_number = int(input("Ingrese el numero de la hoja: "))
width,heigth = Funciones.paper_size(paper_number)
print(f'El ancho y largo de una hoja A{paper_number} es {width},{heigth}')


