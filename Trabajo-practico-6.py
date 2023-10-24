import Funciones
import random
#Ejercicio 1
list_numbers = []
while True:
    number = int(input("Ingrese un numero, para salir ingrese 0: "))
    if number == 0:
        break
    else:
        list_numbers.append(number)
print("La lista de numeros ingresados es: ")
for i in list_numbers:
    print(i)

#Ejercicio 2
number_del = int(input("Ingrese el numero que desea eliminar: "))
count = 0
if number_del in list_numbers:
    list_numbers.remove(number_del)
    print("La nueva lista de numeros es: ")
    for i in list_numbers:
        print(i)  
else:
    print("No es posible eliminar el numero")

#Ejercicio 3
sum_numbers = 0
for i in list_numbers:
    sum_numbers = sum_numbers + i    
print(f'La sumatoria de los numeros de la lista es: {sum_numbers}')  

#Ejercicio 4
largest_number = int(input("Ingrese un numero: "))
new_list = []
for i in list_numbers:
    if i < largest_number:
        new_list.append(i)
print(f'La nueva lista de numeros menores a {largest_number} es: ')
for i in new_list:
    print(i)

#Ejercicio 5
number_ocurrences_list = ()
for number in list_numbers:
    ocurrence = list_numbers.count(number)
    if (number,ocurrence) not in number_ocurrences_list:
        number_ocurrences_list = number_ocurrences_list + ((number,ocurrence),)
print("La lista de los numeros con sus ocurrencias es: ")
for number, ocurrence in number_ocurrences_list:
    print(f'{number}, {ocurrence}')  

#Ejercicio 6
student_primary = Funciones.primary_school_student()
student_secondary = Funciones.secondary_school_student()
print(f'Los estudiantes del nivel primario son: {set(student_primary)}')
print(f'Los estudiantes del nivel secundario son: {set(student_secondary)}')
print(f'Los nombres en el nivel primario son repetidos son {Funciones.repeated_name(student_primary)}')
print(f'Los nombres en el nivel secundario son repetidos son {Funciones.repeated_name(student_secondary)}')
print("Los siguientes nombres del nivel primario no se repiten en el nivel secundario")
for i in student_primary:
    if i not in student_secondary:
        print(i)

#Ejercicio 7
ocurrences = {}
for i in range(0,50):
    word = str(input("Ingrese una palabra: "))
    for character in word:
        if character in ocurrences: 
            ocurrences[character] += 1
        else:
            ocurrences[character] = 1
print("Las ocurrencias de cada caracter en los string ingresados es")            
for character, count in ocurrences.items():
    print(f'{character} : {count}')
#Ejercicio 8
teams = 10
results = [[0] * teams for i in range(teams)]
for i in range(teams):
    for j in range(teams):
        if i != j:
            results[i][j] = random.randint(0,5)

for i in results:
    for j in i:
        print(j, end =' ')
    print(" ")

for i in range(teams):
    points = 0
    victories = 0
    defeats = 0
    ties = 0
    for j in range(teams):
        if results[i][j] > results[j][i]:
            victories += 1
            points += 3
        elif results[i][j] == results[j][i]:   
            ties += 1
            points += 1
        elif results[i][j] < results[j][i]:
            defeats += 1
    print(f'El equipo {i+1} tuvo {victories} victorias, {defeats} derrotas y {ties} empates')   
    print(f'y tuvo un total de {points} puntos')

for i in range(teams):
    goals_scored = 0
    goals_allowed = 0
    goals_scored = sum(results[i]) 
    for j in range(teams):
        goals_allowed += results[j][i]
    print(f'El equipo {i+1} tuvo una diferencia de {goals_scored - goals_allowed} goles')          

#Ejercicio 9
row = 4
col = 4
Funciones.play(row,col)

#Ejercicio 10
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal = [matrix[i][i] for i in range(len(matrix))]
reverse_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(f'La diagonal principal es: {diagonal}')
print(f'La diagonal invertida es: {reverse_diagonal}')

#Ejercicio 11
symbol = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
entry = input("Ingrese la divisa: ")
if entry in symbol:
    print(f'El simbolo de {entry} es {symbol[entry]}')
else:
    print(f'La divisa "{entry}" no esta en la lista')

#Ejercicio 12
name = str(input("Ingrese su nombre: "))
age = int(input("Ingrese su edad:"))
address = str(input("Ingrese si direccion: "))    
phone = int(input("Ingrese su numero de telefono: "))
data = {'name': name, 'age': age, 'address': address, 'phone': phone}          
print(f'{data["name"]} tiene {data["age"]}, vive {data["address"]} y su numero de telefono es {data["phone"]}')  

#Ejercicio 13
fruits = {"naranja":500,"manzana":350,"peras":600,"frutillas":1100}
user_fruit = str(input("Ingrese una una fruta: ")).lower()
kilograms = float(input("Ingrese cuantos kilos necesita: "))
if user_fruit in fruits:
    price = fruits[user_fruit] * kilograms
    print(f'{kilograms}kg de {user_fruit} le cuestan ${price}')
else:
    print("La fruta no esta en la lista")    
