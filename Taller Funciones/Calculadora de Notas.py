def calculate_stats(notes):
    """
    Calcula el promedio, la nota más alta y la nota más baja de una lista de notas.
    """
    if not notes:
        return None, None, None

    average = sum(notes) / len(notes)
    highest = max(notes)
    lowest = min(notes)
    return average, highest, lowest

# Demostración
notes_list = [4.5, 3.2, 5.0, 2.8, 3.9, 4.1]
average_note, highest_note, lowest_note = calculate_stats(notes_list)

print(f"Lista de notas: {notes_list}")
print(f"Promedio: {average_note:.2f}")
print(f"Nota más alta: {highest_note}")
print(f"Nota más baja: {lowest_note}")
