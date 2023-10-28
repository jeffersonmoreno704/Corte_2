from PIL import Image
import pytesseract
from googletrans import Translator

def extraer_texto(imagen_path):
    texto = pytesseract.image_to_string(Image.open(imagen_path))
    return texto

def traducir_texto(texto_ingles):
    translator = Translator()
    texto_espanol = translator.translate(texto_ingles, src='en', dest='es').text
    return texto_espanol

def guardar_resultado(texto_ingles, texto_espanol, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(f'Texto en inglés:\n{texto_ingles}\n\n')
        f.write(f'Texto traducido al español:\n{texto_espanol}\n')

imagen_path = 'prueba_ingles.png'
archivo_salida = 'resultado.txt'

texto_ingles = extraer_texto(imagen_path)
texto_espanol = traducir_texto(texto_ingles)
guardar_resultado(texto_ingles, texto_espanol, archivo_salida)
