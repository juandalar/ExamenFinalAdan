import requests
import json

# Cargar configuración desde config.json
with open("modulos/comentarios/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú Principal =====")
    print("1. Ingresar nuevo comentario")
    print("2. Listar comentarios")
    print("3. Obtener comentario por ID")
    print("4. Actualizar comentario")
    print("5. Eliminar comentario")
    print("6. Salir")

def ingresar():
    texto = input("Texto: ")
    email = input("Email: ")
    calificacion = input("Calificación (1-5): ")
    r = requests.post(f"{API}{ENDPOINTS['create']}", json={
        "texto": texto,
        "usuario_email": email,
        "calificacion": int(calificacion)
    })
    print(r.json())

def listar():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    for c in r.json():
        print(c)

def obtener():
    id = input("ID del comentario: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    print(r.json() if r.status_code == 200 else "Comentario no encontrado.")

def actualizar():
    id = input("ID a actualizar: ")
    texto = input("Nuevo texto: ")
    email = input("Nuevo email: ")
    calificacion = input("Nueva calificación: ")
    url = ENDPOINTS["update"].replace("{id}", id)
    r = requests.put(f"{API}{url}", json={
        "texto": texto,
        "usuario_email": email,
        "calificacion": int(calificacion)
    })
    print(r.json())

def eliminar():
    id = input("ID a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1": ingresar()
        elif opcion == "2": listar()
        elif opcion == "3": obtener()
        elif opcion == "4": actualizar()
        elif opcion == "5": eliminar()
        elif opcion == "6": break
        else: print("Opción inválida.")
