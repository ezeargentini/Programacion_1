#Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra.

nombre = "EZEQUIEL ARGENTINI"
nombre_minus = nombre[0] + nombre[1:].lower()

print(f'Mi nombre en minusculas con excepcion a mi inicial es: {nombre_minus}')