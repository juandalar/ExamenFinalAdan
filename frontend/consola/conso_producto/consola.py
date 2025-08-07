import requests
import json

# Cargar configuración desde config.json
with open("modulos/productos/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú Principal =====")
    print("1. Ingresar nuevo producto")
    print("2. Listar productos")
    print("3. Obtener producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

def ingresar():
    nombre = input("nombre: ")
    descripcion = input("descripcion: ")
    categoria = input("categoria: ")
    precio = input("precio: ")

    payload = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "precio": int(precio)
    }

    r = requests.post(f"{API}{ENDPOINTS['create']}", json=payload)
    mostrar_respuesta(r)

def listar():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    mostrar_respuesta(r, listar=True)

def obtener():
    id = input("ID del producto: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    mostrar_respuesta(r)

def actualizar():
    id = input("ID a actualizar: ")
    nombre = input("Nuevo nombre: ")
    descripcion = input("Nueva descripcion: ")
    categoria = input("Nueva categoria: ")
    precio = input("Nuevo precio: ")

    payload = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "precio": int(precio)
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
