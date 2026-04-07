def convert_grade_to_letter(numeric_grade):
    """
    Convierte una nota numérica a su equivalente en letra (A, B, C, D, F).
    Los rangos se definen usando tuplas (nota_min, nota_max, letra).
    """
    grade_ranges = [
        (4.5, 5.0, 'A'),
        (4.0, 4.4, 'B'),
        (3.0, 3.9, 'C'),
        (2.0, 2.9, 'D'),
        (0.0, 1.9, 'F')
    ]

    for min_grade, max_grade, letter in grade_ranges:
        if min_grade <= numeric_grade <= max_grade:
            return letter
    return "N/A" # Para notas fuera de rango (ej. negativas o > 5.0)

def generate_student_report(students_data):
    """
    Genera un reporte de notas por estudiante, incluyendo su nota numérica y su nota en letra.
    `students_data` es una lista de tuplas (nombre, nota_numerica).
    """
    print("\n--- Reporte de Notas de Estudiantes ---")
    for name, numeric_grade in students_data:
        letter_grade = convert_grade_to_letter(numeric_grade)
        print(f"Estudiante: {name}, Nota Numérica: {numeric_grade:.1f}, Nota en Letra: {letter_grade}")
    print("--------------------------------------")

# Demostración
student_grades = [
    ("Sofía", 4.7),
    ("Mateo", 3.5),
    ("Valeria", 2.8),
    ("Diego", 1.5),
    ("Isabella", 4.1),
    ("Sebastián", 3.0),
    ("Camila", 0.5),
    ("Daniel", 5.0)
]

generate_student_report(student_grades)

# Ejemplo con nota fuera de rango
print("\nEjemplo con nota fuera de rango:")
print(f"Nota 5.5: {convert_grade_to_letter(5.5)}")
print(f"Nota -1.0: {convert_grade_to_letter(-1.0)}")
