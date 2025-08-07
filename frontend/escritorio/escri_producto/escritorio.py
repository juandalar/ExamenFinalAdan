import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("modulos/productos/configuracion/config.json") as f:
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
                    c["id"], c["nombre"], c["descripcion"], c.get("categoria", ""), c["precio"]
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_producto():
    dialogo_producto("Crear nuevo producto")

def editar_producto():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un producto.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_producto("Editar producto", valores)

def eliminar_producto():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un producto.")
        return
    id_com = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este producto?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(id_com)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "producto eliminado.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def dialogo_producto(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    nombre = tk.Entry(ventana)
    nombre.grid(row=0, column=1)

    tk.Label(ventana, text="descripcion:").grid(row=1, column=0)
    descripcion = tk.Entry(ventana)
    descripcion.grid(row=1, column=1)

    tk.Label(ventana, text="categoria:").grid(row=2, column=0)
    categoria = tk.Entry(ventana)
    categoria.grid(row=2, column=1)

    tk.Label(ventana, text="precio:").grid(row=3, column=0)
    precio = tk.Entry(ventana)
    precio.grid(row=3, column=1)

    if datos:
        id_com, nombre_val, descripcion_val, categoria_val, precio_val = datos
        nombre.insert(0, nombre_val)
        descripcion.insert(0, descripcion_val)
        categoria.insert(0, categoria_val)
        precio.insert(0, precio_val)

    def guardar():
        payload = {
            "nombre": nombre.get(),
            "descripcion": descripcion.get(),
            "categoria": categoria.get(),
            "precio": float(precio.get())
        }
        try:
            if datos:
                r = requests.put(API + ENDPOINTS["update"].replace("{id}", str(id_com)), json=payload)
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

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, columnspan=2, pady=10)

# Ventana principal
root = tk.Tk()
root.title("Gestión de productos")

# Tabla
cols = ("ID", "Nombre", "descripcion", "categoria", "precio")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=120)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nuevo", command=crear_producto).pack(side="left", padx=5)
tk.Button(botonera, text="Editar", command=editar_producto).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar", command=eliminar_producto).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar", command=recargar_datos).pack(side="left", padx=5)

recargar_datos()
root.mainloop()
