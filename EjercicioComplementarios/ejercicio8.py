"""
Ahora, intenta calcular el precio final aplicando el descuento al precio original y
almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
aplicar la lógica de matemáticas.
"""

precio_remera = 8999.95
print(f'El precio de la remera es {precio_remera}$')

descuento = 0.15
precio_final = precio_remera * (1.0 - descuento)
print(f'El precio final de la remera con el descuento del {descuento * 100}% es de {precio_final:.2f}$')