from gtts import gTTS

def leer_archivo_y_convertir_voz(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        texto = f.read()

    # Crea un objeto gTTS y convierte el texto a voz
    voz = gTTS(texto)

    # Guarda el audio en el archivo de salida
    voz.save(archivo_salida)

archivo_entrada = 'texto.txt'
archivo_salida = 'audio.mp3'

leer_archivo_y_convertir_voz(archivo_entrada, archivo_salida)
