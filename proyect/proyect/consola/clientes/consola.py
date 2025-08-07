import requests
import json

# Cargar configuración desde config.json
with open("modulos/clientes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Gestión de Clientes - Barbería =====")
    print("1. Registrar nuevo cliente")
    print("2. Listar todos los clientes")
    print("3. Obtener cliente por ID")
    print("4. Actualizar datos de cliente")
    print("5. Eliminar cliente")
    print("6. Salir")

def registrar():
    print("\n--- Registrar Nuevo Cliente ---")
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    telefono = input("Teléfono (opcional): ")
    password = input("Contraseña: ")
    
    payload = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "password": password
    }
    
    try:
        r = requests.post(f"{API}{ENDPOINTS['create']}", json=payload)
        if r.status_code == 200:
            print("✅ Cliente registrado exitosamente!")
            print(r.json())
        else:
            print("❌ Error al registrar cliente:")
            print(r.json())
    except Exception as e:
        print(f"Error de conexión: {e}")

def listar():
    print("\n--- Lista de Clientes ---")
    try:
        r = requests.get(f"{API}{ENDPOINTS['read_all']}")
        if r.status_code == 200:
            clientes = r.json()
            if clientes:
                print(f"{'ID':<5} {'Nombre':<20} {'Email':<25} {'Teléfono':<15} {'Activo':<8} {'Fecha Registro'}")
                print("-" * 90)
                for c in clientes:
                    fecha_registro = c.get('fecha_registro', 'N/A')
                    if isinstance(fecha_registro, str) and 'T' in fecha_registro:
                        fecha_registro = fecha_registro.split('T')[0]
                    
                    print(f"{c.get('id', 'N/A'):<5} {c.get('nombre', 'N/A'):<20} {c.get('email', 'N/A'):<25} "
                          f"{c.get('telefono', 'N/A'):<15} {c.get('activo', 'N/A'):<8} {fecha_registro}")
            else:
                print("No hay clientes registrados.")
        else:
            print("Error al obtener clientes.")
    except Exception as e:
        print(f"Error de conexión: {e}")

def obtener():
    print("\n--- Buscar Cliente por ID ---")
    id_cliente = input("ID del cliente: ")
    
    try:
        url = ENDPOINTS["read_one"].replace("{id}", id_cliente)
        r = requests.get(f"{API}{url}")
        
        if r.status_code == 200:
            cliente = r.json()
            print("\n--- Información del Cliente ---")
            print(f"ID: {cliente.get('id')}")
            print(f"Nombre: {cliente.get('nombre')}")
            print(f"Email: {cliente.get('email')}")
            print(f"Teléfono: {cliente.get('telefono')}")
            print(f"Activo: {'Sí' if cliente.get('activo') else 'No'}")
            print(f"Fecha de Registro: {cliente.get('fecha_registro')}")
        else:
            print("❌ Cliente no encontrado.")
    except Exception as e:
        print(f"Error de conexión: {e}")

def actualizar():
    print("\n--- Actualizar Datos de Cliente ---")
    id_cliente = input("ID del cliente a actualizar: ")
    
    # Primero obtener datos actuales
    try:
        url_get = ENDPOINTS["read_one"].replace("{id}", id_cliente)
        r_get = requests.get(f"{API}{url_get}")
        
        if r_get.status_code != 200:
            print("❌ Cliente no encontrado.")
            return
            
        cliente_actual = r_get.json()
        print(f"\nDatos actuales del cliente:")
        print(f"Nombre: {cliente_actual.get('nombre')}")
        print(f"Email: {cliente_actual.get('email')}")
        print(f"Teléfono: {cliente_actual.get('telefono')}")
        
        print("\nIngrese los nuevos datos (presione Enter para mantener el valor actual):")
        nuevo_nombre = input(f"Nuevo nombre [{cliente_actual.get('nombre')}]: ") or cliente_actual.get('nombre')
        nuevo_email = input(f"Nuevo email [{cliente_actual.get('email')}]: ") or cliente_actual.get('email')
        nuevo_telefono = input(f"Nuevo teléfono [{cliente_actual.get('telefono')}]: ") or cliente_actual.get('telefono')
        nueva_password = input("Nueva contraseña: ")
        
        payload = {
            "nombre": nuevo_nombre,
            "email": nuevo_email,
            "telefono": nuevo_telefono,
            "password": nueva_password
        }
        
        url_update = ENDPOINTS["update"].replace("{id}", id_cliente)
        r = requests.put(f"{API}{url_update}", json=payload)
        
        if r.status_code == 200:
            print("✅ Cliente actualizado exitosamente!")
            print(r.json())
        else:
            print("❌ Error al actualizar cliente:")
            print(r.json())
            
    except Exception as e:
        print(f"Error de conexión: {e}")

def eliminar():
    print("\n--- Eliminar Cliente ---")
    id_cliente = input("ID del cliente a eliminar: ")
    
    # Mostrar datos del cliente antes de eliminar
    try:
        url_get = ENDPOINTS["read_one"].replace("{id}", id_cliente)
        r_get = requests.get(f"{API}{url_get}")
        
        if r_get.status_code != 200:
            print("❌ Cliente no encontrado.")
            return
            
        cliente = r_get.json()
        print(f"\n¿Está seguro que desea eliminar al cliente?")
        print(f"Nombre: {cliente.get('nombre')}")
        print(f"Email: {cliente.get('email')}")
        
        confirmacion = input("\n¿Confirmar eliminación? (s/N): ").lower()
        
        if confirmacion == 's':
            url_delete = ENDPOINTS["delete"].replace("{id}", id_cliente)
            r = requests.delete(f"{API}{url_delete}")
            
            if r.status_code == 200:
                print("✅ Cliente eliminado exitosamente!")
                print(r.json())
            else:
                print("❌ Error al eliminar cliente:")
                print(r.json())
        else:
            print("Eliminación cancelada.")
            
    except Exception as e:
        print(f"Error de conexión: {e}")

def mostrar_estadisticas():
    print("\n--- Estadísticas Rápidas ---")
    try:
        r = requests.get(f"{API}{ENDPOINTS['read_all']}")
        if r.status_code == 200:
            clientes = r.json()
            total = len(clientes)
            activos = len([c for c in clientes if c.get('activo', True)])
            inactivos = total - activos
            
            print(f"Total de clientes: {total}")
            print(f"Clientes activos: {activos}")
            print(f"Clientes inactivos: {inactivos}")
        else:
            print("Error al obtener estadísticas.")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    print("🏪 Sistema de Gestión de Clientes - Barbería")
    print("=" * 50)
    
    while True:
        menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            obtener()
        elif opcion == "4":
            actualizar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el sistema de gestión de clientes!")
            break
        else:
            print("❌ Opción inválida. Por favor seleccione una opción del 1 al 6.")
        
        input("\nPresione Enter para continuar...")