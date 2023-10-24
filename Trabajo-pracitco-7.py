import Funciones
#Ejercicio 1
list_buble_sort = [12,3,1,5,9,10]
Funciones.bubble_sort(list_buble_sort)
print(f'La lista ordenada de manera ascendente es: {list_buble_sort}')

#Ejercicio 2
words = ["hola", "como", "estas"]
Funciones.order_words_asc_selection(words)
print(f'La lista ordenada es {words}')

#Ejercicio 3
books = [
    {"author":"Gabriel Garcia Marquez", "tittle":"El amor en tiempo del colera","year":"1985"},
    {"author":"Gabriel Garcia Marquez", "tittle":"100 años en soledad","year":"1967"},
    {"author":"Harper Lee", "tittle":"To Kill a Mockingbird","year":"1960"},
    {"author":"George orwell", "tittle":"1984","year":"1949"},
    {"author":"Jane Austen", "tittle":"Pride and Prejudice","year":"1813"}
]
books = Funciones.order_books_by_year(books)
for i in range(len(books)):
    print(books[i])

#Ejercico 4
string_list = ["chau","hasta luego","buen dia","hola"]
Funciones.order_string_len_asc(string_list)
for i in range(len(string_list)):
    print(string_list[i])

#Ejercicio 5
numbers_list = [12,3,1,5,9,10]
Funciones.order_numbers_list_asc(numbers_list)
print(numbers_list)    

#Ejercicio 6
numbers_list = [45,80,1,6,3,10]
sorted_number_list = Funciones.order_number_list_by_count(numbers_list)
print(sorted_number_list)

#Ejercicio 7
mixed_list = [3,1,"banana",2,"manzana",0]
sorted_mixed_list = sorted(mixed_list, key=Funciones.order_mixed_list)
print(sorted_mixed_list)

#Ejercicio 8
list_number =[45,21,98,102,12,1]
sorted_list_number = Funciones.merge_sort(list_number)
print(sorted_list_number)



