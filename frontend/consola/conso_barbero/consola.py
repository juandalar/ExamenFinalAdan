import requests
import json

# Cargar configuración desde config.json
with open("modulos/barberos/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú Principal =====")
    print("1. Ingresar nuevo barbero")
    print("2. Listar barberos")
    print("3. Obtener barbero por ID")
    print("4. Actualizar barbero")
    print("5. Eliminar barbero")
    print("6. Salir")

def ingresar():
    nombre = input("nombre: ")
    correo = input("correo: ")
    especialidad = input("especialidad: ")
    telefono = input("telefono: ")

    payload = {
        "nombre": nombre,
        "correo": correo,
        "especialidad": especialidad,
        "telefono": int(telefono)
    }

    r = requests.post(f"{API}{ENDPOINTS['create']}", json=payload)
    mostrar_respuesta(r)

def listar():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    mostrar_respuesta(r, listar=True)

def obtener():
    id = input("ID del barbero: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    mostrar_respuesta(r)

def actualizar():
    id = input("ID a actualizar: ")
    nombre = input("Nuevo nombre: ")
    correo = input("Nueva correo: ")
    especialidad = input("Nueva especialidad: ")
    telefono = input("Nuevo telefono: ")

    payload = {
        "nombre": nombre,
        "correo": correo,
        "especialidad": especialidad,
        "telefono": int(telefono)
    }

    url = ENDPOINTS["update"].replace("{id}", id)
    r = requests.put(f"{API}{url}", json=payload)
    mostrar_respuesta(r)

def eliminar():
    id = input("ID a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    mostrar_respuesta(r)

def mostrar_respuesta(r, listar=False):
    print(f"Status: {r.status_code}")
    try:
        data = r.json()
        if listar and isinstance(data, list):
            for item in data:
                print(item)
        else:
            print(data)
    except Exception:
        print("❌ Respuesta no es JSON válido:", r.text)

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            obtener()
        elif opcion == "4":
            actualizar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
