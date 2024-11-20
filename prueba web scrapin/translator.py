from googletrans import Translator

def traducir_texto(texto, idioma_destino='es'):
    """
    Traduce el texto dado al idioma objetivo.
    
    :param texto: El texto que se va a traducir.
    :param idioma_destino: El código del idioma al que se desea traducir (por defecto 'es' para español).
    :return: El texto traducido al idioma objetivo.
    """
    translator = Translator()
    try:
        traduccion = translator.translate(texto, dest=idioma_destino)
        return traduccion.text
    except Exception as e:
        print(f"Error al traducir el texto: {e}")
        return texto  # Si hay un error, devolver el texto original

# Ejemplo de uso
texto_original = "Hello, how are you?"
texto_traducido = traducir_texto(texto_original, 'es')
print(texto_traducido)  # Imprimirá "Hola, ¿cómo estás?"
