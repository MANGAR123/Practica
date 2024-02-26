def reg_invitados(archivo):
    nombre = input("Ingrese su nombre: ")

    try:
        with open(archivo, 'x') as f:
            f.write(nombre + '\n')
            print(f"Bienvenido, {nombre}! Su nombre ha sido registrado.")
    except FileExistsError:
        print("El archivo ya existe. Utilice otro modo de escritura.")

    with open(archivo, 'w') as f:
        f.write(nombre + '\n')
        print(f"Bienvenido, {nombre}! Su nombre ha sido registrado.")

    with open(archivo, 'a') as f:
        f.write(nombre + '\n')
        print(f"Bienvenido, {nombre}! Su nombre ha sido registrado.")

def consulta_lines_with(archivo):
    with open(archivo, 'r') as f:
        lineas = [linea.strip() for linea in f]
    print("Contenido del archivo:")
    for linea in lineas:
        print(linea)
def main():
    archivo = 'invitados.txt'

    reg_invitados(archivo)

    consulta_lines_with(archivo)

if __name__ == "__main__":
    main()
