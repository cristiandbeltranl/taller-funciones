def word_frequency(word_list):
    """
    Dada una lista de palabras, construye un diccionario con la frecuencia de aparición de cada una.
    """
    frequency_dict = {}
    for word in word_list:
        # Convertir a minúsculas para un conteo no sensible a mayúsculas/minúsculas
        clean_word = word.lower()
        frequency_dict[clean_word] = frequency_dict.get(clean_word, 0) + 1
    return frequency_dict

# Demostración
palabras = ["Python", "es", "un", "lenguaje", "de", "programación", "Python", "es", "divertido", "y", "potente", "programación"]

frequencies = word_frequency(palabras)

print(f"Lista de palabras: {palabras}")
print("\nFrecuencia de cada palabra:")
for word, count in frequencies.items():
    print(f"'{word}': {count}")
