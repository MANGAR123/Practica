def consulta_raw(archivo):
    # Abre el archivo en modo lectura sin la sentencia with
    f = open(archivo, 'r')
    # Lee todo el contenido en una sola variable
    contenido = f.read()
    # Muestra por pantalla el contenido de la variable
    print("Consulta Raw:")
    print(contenido)
    # Cierra el archivo
    f.close()

def consulta_lines(archivo):
    # Abre el archivo en modo lectura sin la sentencia with
    f = open(archivo, 'r')
    # Accede al archivo línea por línea y muestra el contenido de cada línea
    print("Consulta Líneas:")
    for linea in f:
        print(linea.strip())
    # Cierra el archivo
    f.close()

def consulta_lines_with(archivo):
    # Abre el archivo en modo lectura con la sentencia with
    with open(archivo, 'r') as f:
        # Lee el archivo línea por línea y almacena cada línea en una lista
        lineas = [linea.strip() for linea in f]

    # Muestra el contenido de las líneas al finalizar el volcado
    print("Consulta Líneas con With:")
    for linea in lineas:
        print(linea)

# Programa principal
def main():
    archivo = 'consulta.txt'

    # Llama a las tres funciones para consultar el archivo
    consulta_raw(archivo)
    print("\n---\n")
    consulta_lines(archivo)
    print("\n---\n")
    consulta_lines_with(archivo)

if __name__ == "__main__":
    main()
