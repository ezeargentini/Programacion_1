import Funciones

import random

list_word = ["java", "python", "javascript", "php"]
word = random.choice(list_word)
dynamic_word = ["_"] * len(word)
tries = 6

print(f'Inicio de partida')
print(f'{" ".join(dynamic_word)}')

while word != "".join(dynamic_word):
    letter = input("Ingrese una letra: ").lower()
    dynamic_word, tries = Funciones.check_letter(word, letter,dynamic_word,tries)
    print(f'El avance de la palabra es: {" ".join(dynamic_word)}, le quedan {tries} intentos')
    if tries == 0 and word != "".join(dynamic_word):
        print(f'Se quedo sin intentos, la palabra era {word}')
        break

if word == "".join(dynamic_word):
    print(f'Felicitaciones adivino la palabra le sobraron {tries} intentos')