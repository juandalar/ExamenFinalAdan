import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("modulos/clientes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def recargar_datos():
    for item in tree.get_children():
        tree.delete(item)
    try:
        r = requests.get(API + ENDPOINTS["read_all"])
        if r.status_code == 200:
            for c in r.json():
                tree.insert("", "end", values=(
                    c["id"], c["nombre"], c["email"], c["telefono"], c.get("activo", True), c.get("fecha_registro", "")
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_cliente():
    dialogo_cliente("Crear nuevo cliente")

def editar_cliente():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un cliente.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_cliente("Editar cliente", valores)

def eliminar_cliente():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un cliente.")
        return
    id_cliente = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este cliente?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(id_cliente)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "Cliente eliminado.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def dialogo_cliente(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)
    ventana.geometry("400x300")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    nombre = tk.Entry(ventana, width=30)
    nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    email = tk.Entry(ventana, width=30)
    email.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    telefono = tk.Entry(ventana, width=30)
    telefono.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Contraseña:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    password = tk.Entry(ventana, width=30, show="*")
    password.grid(row=3, column=1, padx=5, pady=5)

    # Checkbox para activo (solo en edición)
    activo_var = tk.BooleanVar()
    if datos:
        tk.Label(ventana, text="Activo:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        activo_check = tk.Checkbutton(ventana, variable=activo_var)
        activo_check.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    if datos:
        id_cliente, nombre_val, email_val, telefono_val, activo_val, _ = datos
        nombre.insert(0, nombre_val)
        email.insert(0, email_val)
        telefono.insert(0, telefono_val)
        activo_var.set(activo_val)
        # En edición, no mostrar campo de contraseña
        password.grid_remove()
        tk.Label(ventana, text="(Contraseña sin cambios)").grid(row=3, column=1, padx=5, pady=5)

    def guardar():
        if not nombre.get() or not email.get():
            messagebox.showwarning("Campos requeridos", "Nombre y email son obligatorios.")
            return
            
        payload = {
            "nombre": nombre.get(),
            "email": email.get(),
            "telefono": telefono.get()
        }
        
        if not datos:  # Solo agregar password en creación
            if not password.get():
                messagebox.showwarning("Campo requerido", "La contraseña es obligatoria.")
                return
            payload["password"] = password.get()
        else:  # En edición, agregar estado activo
            payload["activo"] = activo_var.get()
            
        try:
            if datos:
                r = requests.put(API + ENDPOINTS["update"].replace("{id}", str(id_cliente)), json=payload)
            else:
                r = requests.post(API + ENDPOINTS["create"], json=payload)
            if r.status_code in [200, 201]:
                recargar_datos()
                ventana.destroy()
                messagebox.showinfo("Éxito", "Operación exitosa.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar", command=guardar, bg="lightblue").grid(row=5, columnspan=2, pady=20)

# Ventana principal
root = tk.Tk()
root.title("Gestión de Clientes - Barbería")
root.geometry("900x600")

# Título
titulo = tk.Label(root, text="Sistema de Gestión de Clientes", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Tabla
cols = ("ID", "Nombre", "Email", "Teléfono", "Activo", "Fecha Registro")
tree = ttk.Treeview(root, columns=cols, show="headings", height=15)

# Configurar columnas
tree.heading("ID", text="ID")
tree.column("ID", anchor="center", width=50)

tree.heading("Nombre", text="Nombre")
tree.column("Nombre", anchor="w", width=150)

tree.heading("Email", text="Email")
tree.column("Email", anchor="w", width=200)

tree.heading("Teléfono", text="Teléfono")
tree.column("Teléfono", anchor="center", width=120)

tree.heading("Activo", text="Activo")
tree.column("Activo", anchor="center", width=70)

tree.heading("Fecha Registro", text="Fecha Registro")
tree.column("Fecha Registro", anchor="center", width=150)

# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Empaquetar tabla y scrollbar
tree.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nuevo Cliente", command=crear_cliente, bg="lightgreen", width=15).pack(side="left", padx=5)
tk.Button(botonera, text="Editar Cliente", command=editar_cliente, bg="lightyellow", width=15).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar Cliente", command=eliminar_cliente, bg="lightcoral", width=15).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar Datos", command=recargar_datos, bg="lightblue", width=15).pack(side="left", padx=5)

# Cargar datos iniciales
recargar_datos()
root.mainloop()