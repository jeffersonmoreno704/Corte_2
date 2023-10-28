import random
import string
import os

def generar_contraseña():
    # Obtenemos una lista de caracteres válidos para la contraseña.
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Generamos una contraseña de longitud aleatoria, al menos 8 caracteres.
    longitud = random.randint(8, 20)
    contraseña = ""
    for _ in range(longitud):
        contraseña += caracteres[random.randint(0, len(caracteres) - 1)]

    # Eliminamos los espacios en blanco de la contraseña.
    contraseña = contraseña.replace(" ", "")

    return contraseña

def guardar_contraseña(contraseña):
    # Creamos el archivo de texto si no existe.
    if not os.path.exists(contraseña):
        with open("contraseñas.txt", "w") as f:
            f.write("")

    # Guardamos la contraseña en el archivo.
    with open("contraseñas.txt", "a") as f:
        f.write(contraseña + "\n")

def main():
    # Generamos la contraseña.
    contraseña = generar_contraseña()

    # Mostramos la contraseña en consola.
    print(contraseña)

    # Guardamos la contraseña en un archivo de texto plano.
    guardar_contraseña(contraseña)

if __name__ == "__main__":
    main()