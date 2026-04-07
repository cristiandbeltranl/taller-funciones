def get_approved_students(students_grades):
    """
    Dada una lista de tuplas (nombre, nota), devuelve solo los estudiantes aprobados (nota >= 3.0).
    """
    approved_students = []
    for name, grade in students_grades:
        if grade >= 3.0:
            approved_students.append((name, grade))
    return approved_students

# Demostración
students = [
    ("Ana", 4.0),
    ("Juan", 2.5),
    ("Maria", 3.8),
    ("Pedro", 1.9),
    ("Luisa", 3.0)
]

approved = get_approved_students(students)

print(f"Todos los estudiantes: {students}")
print(f"Estudiantes aprobados: {approved}")
