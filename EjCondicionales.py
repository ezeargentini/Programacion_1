"""
Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se
dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.
"""

dia_completo = input("Ingrese el dia(dia semana,DD/MM): ")

coma = dia_completo.find(",")
dia_semana = dia_completo[0:coma]
dia = int(dia_completo[coma+2:coma+4])
mes = int(dia_completo[coma+5:])

dia_semana = dia_semana.lower()

if (dia <= 31) and (mes <= 12):
    if (dia_semana == "lunes") or (dia_semana == "martes") or (dia_semana == "miércoles"):
        examen = input(f"Ingrese si hubo examen el día {dia_semana}, {dia:02d}/{mes:02d}: ")
        if examen.lower() == "si":
            cant_aprobado = int(input("Ingrese cuántos alumnos aprobaron: "))
            cant_desaprobado = int(input("Ingrese cuántos alumnos desaprobaron: "))
            promedio = (cant_aprobado / (cant_aprobado + cant_desaprobado)) * 100
            print(f'El promedio de alumnos aprobados es: {promedio:.2f}%')
    elif dia_semana == "jueves":
            asistencia = float(input("Ingrese cuál es el porcentaje de asistencia: "))
            if asistencia >= 50:
                print("Asistió la mayoría")
            elif asistencia < 50:
                print("No asistió la mayoría")
    elif dia_semana == "viernes" and dia == 1 and (mes == 1 or mes == 7):
            print("Comienzo nuevo ciclo")
            cant_alumno_viajero = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_alumno_viajero = float(input("Ingrese el arancel por alumno: "))
            total = cant_alumno_viajero * arancel_alumno_viajero
            print(f'El ingreso total es de ${total:.2f}')
    else:
        print("Fin de Semana, No hay clases")
else:
    print("Fecha inválida")

