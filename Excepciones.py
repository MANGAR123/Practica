print('Practica excepciones: inicio')

while True:
    try:
        num = int(input('Ingrese el numerador: '))
        denom = int(input('Ingrese el denominador: '))

        division = num / denom
        print('División = %6.2f' % division)
        break  # Salir del bucle si la división se realiza con éxito

    except ValueError:
        print('Error: Por favor ingrese valores enteros.')
    except ZeroDivisionError:
        print('Error: El denominador no puede ser cero.')
    except Exception as e:
        print(f'Error inesperado: {e}')

print('Adiós')

