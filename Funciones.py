import math
import sys
import random
#Suma los digitos de un numero
def add_digits(number):
    mod = 0
    while number != 0:
        mod = mod + number % 10
        number = number // 10
    return mod

#Retorna el mayor
def most(a,b):
    if(a>b):
        return a
    else:
        return b  

#Retorne el menor
def least(a,b):
    if(a<b):
        return a
    else:
        return b   

#Chequea si una letra esta en un lista, en el caso que no este descuenta un intento
def check_letter(word, letter,dynamic_word,tries):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            dynamic_word[i] = letter
            count += 1
    if count >= 1:
        print("Adivinaste una letra")
    elif count == 0:
        print("La letra no estaba en la palabra")
        tries -= 1
    return dynamic_word, tries

#Chequea si un dni es valido
def id_number(dni):
    dni = str(dni)
    if(len(dni) == 8 or len(dni) == 7):
        return True
    else:
        return False

#Devuelve la longitud de la ultima palabra de una frase
def len_word(phrase):
    phrase = phrase.strip()
    word = phrase.split(" ")
    last_word = word[-1]    
    length_last_word = len(last_word)
    return length_last_word       

#Esta funcion realiza el ingreso de datos de socios
def socios_registry():
    print("Para salir de esta seccion ingrese el primer nombre vacio")
    name_one = input("Ingrese el primer nombre del socio: ")
    if len(name_one) != 0:
        name_two = input("Ingrese el segundo nombre del socio(Si no tiene presione enter): ")
        surname = input("Ingrese el apellido del socio: ")
        dni = int(input("Ingrese el dni del socio: "))
        while id_number(dni) == False:
                print("Ingreso un dni invalido, intente nuevamente")
                dni = int(input("Ingrese el dni del socio: "))
        if len(name_two) > 0:
            name_complete = name_one + " " + name_two + " "+ surname
            return name_complete, dni
        elif len(name_two) == 0:
            name_complete = name_one + " "+ surname 
            return name_complete, dni
    else:
        return False, False
    
#Generador de id con el primer nombre de una persona y los primeros 3 digitos del dni
def generator_id(name_complete, dni):
    name_parts = name_complete.split()
    name_one = name_parts[0]
    dni_string = str(dni)
    three_digits = dni_string[:3] 
    id = name_one + three_digits
    return id

#Recibe dos numero y verifica si son multiplos
def is_multiple(number_one, number_two):
        if number_one % number_two == 0:
            return True
        else:
            return False

#Realiza el promedio de dos temperaturas
def average_temperature(temperature_min, temperature_max):
    avg_temperature = (temperature_max + temperature_min) / 2
    return avg_temperature

#Recibe un text y devuelve un espacio despues de cada letra
def converted_text(text):
    spaced_text = ""
    for i in text:
        if i != " ": #Verifica que en la posicion no haya un espacio
            spaced_text = spaced_text + i + " "
        else:
            spaced_text = spaced_text + i    
    return spaced_text.strip()

#Devuelve el numero minimo y maximo de una lista 
def min_and_max_number(number_list):
    number_min = sys.maxsize
    number_max = -sys.maxsize - 1
    for i in number_list:
        if i > number_max:
            number_max = i
        
        if i < number_min:
            number_min = i
    return number_min, number_max    
        
#Retorna el area y el perimetro de una circunferencia        
def area_and_perimeter(radius):
    area = math.pi * math.pow(radius, 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter

#Retorna true si el usuario y contraseña son correctos 
def check_login(user, password):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        return False
    

#Recibe un diccionario con producto, su precio y su descuento y devuelve el total de la compra
def price_final_buy(cart):
    total_final_price = 0
    for product, (price, percentage) in cart.items():
        discount_price = price - ((price * percentage) / 100)
        total_final_price += discount_price
    return total_final_price    

#Esta funcion recibe una funcion(Calcula el cuadrado) y una lista de numeros
def processin_list(square, number_list):
    results = []
    for i in number_list:
        result = square(i)
        results.append(result)
    return results    

#Funcion para calcular el cuadrado de un numero
def square(number):
    return number ** 2

#Recibe una frase y devuelve un diccionario con cada palabra y su longitud
def diccionary_len_phrase(phrase):
    words = phrase.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths    

#Recibe un vector y calcula su modulo
def calculate_module(vector):
    result = 0
    for i in vector:
        result += i ** 2
    return math.sqrt(result)    

#Verifica si un numero es primo
def is_prime(number):
    if number <= 1 or number % 2 == 0:
        return False
    if number == 2:
        return True
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False       
    return True    

#Calcula el factorial de un numero
def factorial(number):
    factorial = 1
    if number < 0:
        return "No se puede calcular numero negativos"
    elif number == 0:
        return factorial
    else:
        for i in range(1, number + 1):
            factorial *= i
        return factorial

#Calcula la frecuencia de un digito en un numero
def calculate_frequency(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    frequency = 0
    for i in number_str:
        if i == digit_str:
            frequency += 1
    return int(frequency)

#Añade un pasajero a una lista
def add_passengers(list_passengers):
    name = str(input("Ingrese el nombre completo del pasajero: "))
    id = int(input("Ingrese el dni del pasajero: "))
    destination = str(input("Ingrese el destino del pasajero: "))
    passengers_info = (name,id,destination)
    list_passengers.append(passengers_info)

#Añade un destino a una lista
def add_destinations(list_destinations):
    city = str(input("Ingrese la ciudad de destino: "))
    country = str(input("Ingrese el pais de destino: "))
    destinations_info = (city, country)
    list_destinations.append(destinations_info)

#Recibe un dni y una lista y returna el destino del pasajero
def destination_passenger(id, list_passengers):
    for name, id_number, destination in list_passengers:
        if id_number == id:
            return destination
    return False

#Retorna la cantidad de pasajeros que viajan a una ciudad    
def cant_passenger_destination(destination, list_passenger):
    count = 0
    for name, dni, city in list_passenger:
        if city == destination:
            count += 1
    return count

#Retorna el destino al que viaja un pasajero
def country_destination_passenger(id_number, list_passenger, list_destination):
    for name,dni,city in list_passenger:
        if id_number == dni:
            city_passenger = city
            for city_destination, country in list_destination:
                if city_passenger == city_destination:
                    return country 

#Retorna la cantidad de pasajeros que viajan a un pais
def cant_country_passenger(country, list_passenger, list_destination):
    count = 0
    for name,dni,city in list_passenger:
        for city_destination, country in list_destination:
            if city == city_destination:
                count += 1         
    return count

#Recibe una lista de ventas con direcciones de clientes y retorna una lista con las 
#direcciones sin repetir
def get_unique_address(sales):
    unique_addres = []
    for name,day,price,address in sales:
        if address not in unique_addres:
            unique_addres.append(address)
    return unique_addres

#Retorna la longitud de una lista de socios
def cant_members(registred_members):
    return len(registred_members)

#Paga las cuotas adeudas de un socio
def dues_payment(number_member, registred_members):
    if number_member in registred_members:
        registred_members[number_member]["Cuota_al_dia"] = True
        print(f'El socio {number_member} ha pagado todas las cuotas adeudadas')
    else:
        print(f'El numero de socio {number_member} no existe')    

#Si la fecha de ingreso es 13/03/2018 la cambia a 14/03/2018
def modify_admission_date(number_member, registred_members):
    for i in registred_members:
        if registred_members[number_member]["Fecha_ingreso"] == "13/03/2018":
            registred_members[number_member]["Fecha_ingreso"] = "14/03/2018"

#Recibe el nombre de un socio y lo elimina de la lista
def delete_member(name, registred_members):
    for number_member, data_member in registred_members.items():
        if data_member["nombre"] == name:
            del registred_members[number_member]
            return registred_members
    print("No se encontro el nombre del socio")

#Imprime un diccionario de socios
def print_list(registred_members):
    print("\nListado de socios:")
    for number_member, data_member in registred_members.items():
        print(f"Socio n°{number_member}, {data_member['nombre']}, ingresó: {data_member['Fecha_ingreso']}, cuota {data_member['Cuota_al_dia']}.")
    
#Añade el nombre de pila de estudiantes de nivel primario a una lista 
def primary_school_student():
    list_student_primary = []
    print("**** Estudiantes nivel primario ****")
    while True:
        name = str(input("Ingrese el nombre de pila del alumno, para salir ingrese x: "))
        if name.lower() == 'x':
            break
        else:
            list_student_primary.append(name)
    return list_student_primary

#Añade el nombre de pila de estudiantes de nivel secundario a una lista
def secondary_school_student():
    list_student_secondary = [] 
    print("**** Estudiantes nivel secundario ****")
    while True:       
        name = str(input("Ingrese el nombre de pila del alumno, para salir ingrese x: "))
        if name.lower() == 'x':
            break
        else:
            list_student_secondary.append(name)
    return list_student_secondary

#Recibe una lista de estudiantes y retorna los nombres que se repiten
def repeated_name(list_student):
    list_repeated_names = []
    count = 0
    for i in list_student:
        count = list_student.count(i)
        if i not in list_repeated_names and count > 1:
            list_repeated_names.append(i)
    return list_repeated_names

#Ordena una lista a traves del ordenamiento de burbuja
def bubble_sort(list):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
                sorted = False
    return list

#Ordena una lista a traves del ordenamiento de seleccion
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(len(list)):
            if list[min_index] > list[j]:
                min_index = j
            list[i],list[min_index] = list[min_index], list[i]
    return list        

#Ordena una lista a traves del ordenamiento de insercion
def insert_sort(list):
    for i in range(1,len(list)):
        actual = list[i]
        j = i - 1
        while j >= 0 and list[j] > actual:
            list[j+1] = list[j]
            j-=1
        list[j+1] = actual 
    return list    

#Ordena una lista a traves del ordenamiento merge
def merge_sort(list):
    if len(list) == 1:
        return list
    middle = len(list) // 2
    left_list = list[:middle]
    right_list = list[middle:]
    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)
    return merge(sorted_left_list, sorted_right_list)

#Realiza el merge del ordenamiento de la funcion anterior
def merge(left_list, right_list):
    sorted_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            sorted_list.append(right_list[0])
            right_list.pop(0)
        else:
            sorted_list.append(left_list[0])
            left_list.pop(0)    
    while len(left_list) > 0:
            sorted_list.append(left_list[0])
            left_list.pop(0)    
    while len(right_list) > 0:
        sorted_list.append(right_list[0])
        right_list.pop(0)
    return sorted_list  

#Realiza una busqueda lineal
def linear(list, element):
    ix = -1
    for i in range(len(list)):
        if element == list[i]:
            return i
    return ix    

#Reliza una busqueda binaria
def binary(list,low, high, element):
    if high >= low:
        middle = (high + low) // 2
        if list[middle] == element:
            return middle
        elif list[middle] > element:
            return binary(list, low, middle - 1, element)
        else:
            return binary(list, middle + 1, high,element)
    else:
        return -1   

#Retorna cuanto tiempo demora una rata en salir de su jaula, eligiendo caminos al azar
#cada camino demora un tiempo, con el camino 3 sale de la jaula
def mouse_experiment(time):
    path = random.randint(1,3)
    if path == 3:
        time += 7
        return time
    elif path == 1:
        return mouse_experiment(time + 3)
    elif path == 2:
        return mouse_experiment(time + 5)

#Ordena una lista de palabras de manera ascendente a traves del metodo de 
# seleccion     
def order_words_asc_selection(words):    
    n = len(words)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if words[j] < words[min_index]:
                min_index = j
        words[i],words[min_index] = words[min_index], words[i]
    return words  

#Suma la cantidad de digitos de un numero de manera recursiva
def add_digits_recursion(number):
    number_str = str(number)
    if len(number_str) == 1:
        return 1 
    else:
        return 1 + add_digits_recursion(number // 10)

#Devuelve True o False dependiendo si un numero es potencia de otro    
def is_power_of(base,exponent):
    if base == 1:
        return True
    if base < exponent or base % exponent != 0:
        return False
    return is_power_of(base // exponent, exponent)

def find_position(phrase, fragment, start=0,positions=None):
    if positions is None:
        positions = []
    position = phrase.find(fragment, start)
    if position != -1:
        positions.append(position)
        return find_position(phrase, fragment, position + 1, positions)  
    return positions     

def create_board(row, col):
    num_cards = row * col
    cards = list(range(num_cards)) * 2
    random.shuffle(cards)
    board = [[-1] * col for i in range(row)]
    for i in range(row):
        for j in range(col):
            board[i][j] = cards.pop()
    return board

def display_board(board, row, col):
    for i in range(row):
        for j in range(col):
            if board[i][j] == -1:
                print('?', end='\t')
            else:
                print('*', end='\t')    
        print()
                        
def play(row, col):
    board = create_board(row, col)
    display_board(board,row,col)
    tries = 0
    pair_founds = 0
    
    while pair_founds < row * col /2:
        row_one= int(input("Ingrese los valores de fila 1: "))
        col_one = int(input("Ingrese los valores de columna 1: "))
        row_two = int(input("Ingrese los valores de fila 2: "))
        col_two = int(input("Ingrese los valores de columna 2: "))
        if board[row_one][col_one] == board[row_two][col_two] and (row_one != row_two or col_one != col_two):
            print("Encontraste un par!!")
            board[row_one][col_one] = -1
            board[row_two][col_two] = -1
            pair_founds += 1
        else:
            print("No es un par, sigue intenando")
        display_board(board,row,col)
        tries += 1
    print("Felicitaciones eencontraste todos los pares")          

#Ordena una lista de diccionarios de libros con su año a traves de selection sort        
def order_books_by_year(books):
    for i in range(len(books)):
        year_min = books[i]["year"]
        for j in range(len(books)):
            if year_min < books[j]["year"]:
                books[i], books[j] = books[j], books[i]
    return books

#Ordena una lista de cadenas de forma ascendente segun su longitud
def order_string_len_asc(string_list):
    for i in range(1,len(string_list)):
        actual = string_list[i]
        j = i - 1
        while j >= 0 and len(string_list[j]) > len(actual):
            string_list[j+1] = string_list[j]
            j-=1
        string_list[j+1] = actual 
    return string_list    

#Ordena un alista de numeros de manera descendente a traves de bubble sort
def order_numbers_list_desc(numbers_list):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(numbers_list) - 1):
            if numbers_list[i] < numbers_list[i+1]:
                aux = numbers_list[i]
                numbers_list[i] = numbers_list[i+1]
                numbers_list[i+1] = aux
                sorted = False
    return numbers_list

#Ordena una lista de numeros a traves de count sort
def order_number_list_by_count(numbers_list):
    max_value = max(numbers_list)
    min_value = min(numbers_list)
    range_of_values = max_value - min_value + 1

    count = [0] * range_of_values

    for num in numbers_list:
        count[num - min_value] += 1

    sorted_list = []
    for i in range(range_of_values):
        for _ in range(count[i]):
            sorted_list.append(i + min_value)

    return sorted_list     

#Ordena una lista de cadenas y enteros colocando primero los enteros ordenados y segundo las cadenas ordenadas
def order_mixed_list(item):
    if isinstance(item,int):
        return (0,item)
    else:
        return (1,item)

#Funciona en conjunto con odd y determinan la paridad de un numero
def even(number):
    if number == 0:
        return True
    else:
        return odd(number - 1)

def odd(number):
    if number == 0:
        return False
    else:
        return even(number - 1)

#Retorna el mayor numero de una lista
def most_by_list(list_numbers,i=0,most=-sys.maxsize):
    if i == len(list_numbers):
        return most
    else:
        if list_numbers[i] > most:
            most = list_numbers[i]
        return most_by_list(list_numbers, i + 1, most)     

#Replica los numeros de una lista la cantidad de veces que le pidamos
def replicate_numbers(list_numbers, replicate,i=0):
    if i == len(list_numbers):
        return list_numbers
    else:
        list_numbers[i] = [list_numbers[i]] * replicate
        return replicate_numbers(list_numbers,replicate,i+1)

#Realiza una suma recursiva con dos numeros
def recursive_summation(n,p):
    if n == 1:
        return p
    else: 
        return n * p + recursive_summation(n-1,p)
    
#Recibe una fila y una columna y retorna el valor de la fila y columna de un triangulo pascal    
def pascal(row,col):
    if row == 0 or col==row:
        return 1
    else:
        return pascal(row-1,col-1) + pascal(row-1,col)
        
#Recibe una lista de caracteres y su longitud e imprime todas las combinaciones posibles        
def combinations(list_char, length_list,current_string=''):
    if length_list == 0:
        print(current_string)
    else:
        for character in list_char:
            combinations(list_char,length_list -1,current_string+character)    

#Recibe un tamaño de papel segun la norma ISO 216 y devuelve sus medidas
def paper_size(number_paper):
    if number_paper == 0:
        return (841, 1189)
    else:
        width, height = paper_size(number_paper - 1)
        return (height // 2, width)