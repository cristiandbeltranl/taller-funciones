class ContactAgenda:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None):
        """
        Agrega un nuevo contacto a la agenda.
        """
        if name in self.contacts:
            print(f"El contacto {name} ya existe. Actualizando...")
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contacto {name} agregado/actualizado.")

    def find_contact(self, name):
        """
        Busca un contacto por su nombre y devuelve su información.
        """
        if name in self.contacts:
            return self.contacts[name]
        else:
            print(f"El contacto {name} no se encontró.")
            return None

    def delete_contact(self, name):
        """
        Elimina un contacto de la agenda.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contacto {name} eliminado.")
        else:
            print(f"El contacto {name} no se encontró.")

    def list_all_contacts(self):
        """
        Muestra todos los contactos en la agenda.
        """
        if not self.contacts:
            print("La agenda está vacía.")
            return
        print("\n--- Contactos en la Agenda ---")
        for name, info in self.contacts.items():
            print(f"Nombre: {name}, Teléfono: {info['phone']}, Email: {info['email']}")
        print("------------------------------")

# Demostración
agenda = ContactAgenda()
agenda.add_contact("Carlos", "123-456-7890", "carlos@example.com")
agenda.add_contact("Laura", "987-654-3210")
agenda.add_contact("Carlos", "111-222-3333", "carlos.nuevo@example.com") # Actualizar

agenda.list_all_contacts()

print("\nBuscando a Laura:")
laura_info = agenda.find_contact("Laura")
if laura_info:
    print(f"Información de Laura: {laura_info}")

print("\nEliminando a Laura:")
agenda.delete_contact("Laura")
agenda.find_contact("Laura") # Intentar buscarla de nuevo

agenda.list_all_contacts()
