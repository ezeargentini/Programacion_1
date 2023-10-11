import pytest
from Funciones import *

#Test de Funcion check_letter
@pytest.mark.parametrize("word, letter, dynamic_word, tries",[
    ("hola", "a", "____", 9),
    ("hola como estas", "z", "_____________" , 9),
])
def test_check_letter(word, letter, dynamic_word, tries):
    assert check_letter(word, letter, dynamic_word, tries) == dynamic_word, tries

#Test de Funcion id_number
@pytest.mark.parametrize("dni, res",[
    (44820614, True),
    (44820615, False),
    (123, False)
])
def test_id_number(dni, res):
    assert id_number(dni) == res

#Test de Funcion len_word
@pytest.mark.parametrize("phrase, res",[
    ("hola como estas", 5),
    ("hola", 4)
])
def test_len_word(phrase, res):
    assert len_word(phrase) == res

#Test funcion socios_registry (no funciona porque los valores lo pide la funcion)
@pytest.mark.parametrize('input_values, expected_output',[
    (['Jeronimo', 'Felipe' , 'Cortez', 44820614], ('Jeronimo Felipe Cortez', 44820614)),
    (['', 'Felipe' , 'Cortez', 44820614], (False, False))
])
def test_socios_registry(input_values, expected_output):
    assert socios_registry(input_values) == expected_output  

#Test funcion generator_id
@pytest.mark.parametrize("name_complete, dni, res",[
    ('Jeronimo Felipe Cortez', 44820614, 'Jeronimo448'),
    ('Jeronimo Cortez', 44444444, 'Jeronimo444')
])
def test_generator_id(name_complete, dni, res):
    assert generator_id(name_complete, dni) == res  

#Test funcion is_multiple
@pytest.mark.parametrize("number_one, number_two, res",[
    (6, 12, True),
    (12, 6, False)
])
def test_is_multiple(number_one, number_two, res):
    assert is_multiple(number_one, number_two) == res

#Test funcion average_temperture
@pytest.mark.parametrize("temperature_min, temperature_max, res",[
    (10, 20, 15),
    (20, 40, 30)
])
def test_average_temperature(temperature_min, temperature_max, res):
    assert average_temperature(temperature_min, temperature_max) == res

#Test funcion converted_text
@pytest.mark.parametrize("text, res",[
    ("hola", "h o l a"),
    ("chau", "c h a u")
])
def test_converted_text(text, res):
    assert converted_text(text) == res

#Test funcion min_and_max_number
@pytest.mark.parametrize("number_list, res" ,[
    ([14, 2, 3, 4], (1, 4)),
    ([5, 6, 7, 8], (5, 8))
])
def test_min_and_max_number(number_list, res):
    assert min_and_max_number(number_list) == res

#Test funcion area_and_perimeter
@pytest.mark.parametrize("radius, res", [
    (4, (50.26548245743669, 25.132741228718345))
])  
def test_area_and_perimeter(radius, res):
    assert area_and_perimeter(radius) == res

#Test funcion check login
@pytest.mark.parametrize("user, password, res", [
    ("usuario1", "asdasd", True),
    ("usuario1", "asdd", False),
    ("usrio1", "asdasd", False)
])
def test_check_login(user,password,res):
    assert check_login(user, password) == res

#Test funcion final_buy_price
@pytest.mark.parametrize("cart, res",[
    ({"producto" : (100, 10)}, 90),
    ({"producto" : (1000, 10)}, 900)
])
def test_price_final_buy(cart, res):
    assert price_final_buy(cart) == res

#Test funcion processing_list
@pytest.mark.parametrize("function, number_list, res",[
("square", [2,4], [4,8])
])
def test_processing_list(function, number_list, res):
    processin_list(square, number_list) == res

#Test funcion square
@pytest.mark.parametrize("number, res",[
    (2,4)
])    
def test_square(number,res):
    square(number) == res

#Test funcion diccionary_len_phrase
@pytest.mark.parametrize("phrase, res",[
    ("hola como estas", {"hola" : (4), "como" : (4), "estas" : (5)})
])    
def test_diccionary_len_phrase(phrase, res):
    assert diccionary_len_phrase(phrase) == res

#Test funcion calculate_module
@pytest.mark.parametrize("vector, res",[
    ([1,2,3,4], 5.477225575051661)
])    
def test_calculate_module(vector, res):
    calculate_module(vector) == res

#Test funcion is_prime
@pytest.mark.parametrize("number, res",[
    (13, True),
    (4, False)
])    
def test_is_prime(number, res):
    is_prime(number) == res

#Test funcion factorial
@pytest.mark.parametrize("number, res",[
    (5, 120),
    (0, 1),
    (-2, "No se puede calcular numero negativos")
])
def test_factorial(number, res):
    factorial(number) == res

#Test funcion calculate_frequency
@pytest.mark.parametrize("number,digit,res",[
    (2224, 2, 3),
    (123432, 8, 0)
])    
def test_calculate_frequency(number,digit, res):
    calculate_frequency(number,digit) == res




