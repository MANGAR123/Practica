def libro_visitas(archivo):
    with open(archivo, 'a') as f:
        while True:

            nombre = input("Ingrese su nombre (deje vacío para salir): ")

            if not nombre:
                break  # Sale del bucle si se introduce un valor vacío


            f.write(nombre + '\n')
            print(f"Bienvenido, {nombre}! Su visita ha sido registrada.")

def consulta_lines_with(archivo):

    with open(archivo, 'r') as f:

        lineas = [linea.strip() for linea in f]

    print("Contenido del archivo:")
    for linea in lineas:
        print(linea)
def main():
    archivo = 'libro_visitas.txt'

    libro_visitas(archivo)

    consulta_lines_with(archivo)

if __name__ == "__main__":
    main()
