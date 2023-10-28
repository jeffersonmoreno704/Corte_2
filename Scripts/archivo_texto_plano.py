def contar_lineas(archivo):
    with open(archivo, 'r') as f:
        return len(f.readlines())

def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = texto.split()
        return len(palabras)

def contar_caracteres(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        return len(texto)

def contar_apariciones_palabra(archivo, palabra):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = texto.split()
        return palabras.count(palabra)

def generar_informe(archivo_entrada, archivo_salida, palabra_buscar):
    lineas = contar_lineas(archivo_entrada)
    palabras = contar_palabras(archivo_entrada)
    caracteres = contar_caracteres(archivo_entrada)
    apariciones = contar_apariciones_palabra(archivo_entrada, palabra_buscar)

    with open(archivo_salida, 'w') as f:
        f.write(f"Líneas totales: {lineas}\n")
        f.write(f"Palabras totales: {palabras}\n")
        f.write(f"Caracteres totales: {caracteres}\n")
        f.write(f"Apariciones de '{palabra_buscar}': {apariciones}\n")

archivo_entrada = 'texto.txt'
archivo_salida = 'informe.txt'
palabra_buscar = 'Python'

generar_informe(archivo_entrada, archivo_salida, palabra_buscar)
