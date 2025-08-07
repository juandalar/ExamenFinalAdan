import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("modulos/barberias/configuracion/config.json") as f:
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
                    c["id"], c["nombre"], c["direccion"], c.get("ciudad", ""), c["telefono"]
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_barberia():
    dialogo_barberia("Crear nueva barberia")

def editar_barberia():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione una barberia.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_barberia("Editar barberia", valores)

def eliminar_barberia():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione una barberia.")
        return
    id_com = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar esta barberia?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(id_com)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "barberia eliminada.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def dialogo_barberia(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
    nombre = tk.Entry(ventana)
    nombre.grid(row=0, column=1)

    tk.Label(ventana, text="Direccion:").grid(row=1, column=0)
    direccion = tk.Entry(ventana)
    direccion.grid(row=1, column=1)

    tk.Label(ventana, text="Ciudad:").grid(row=2, column=0)
    ciudad = tk.Entry(ventana)
    ciudad.grid(row=2, column=1)

    tk.Label(ventana, text="Telefono:").grid(row=3, column=0)
    telefono = tk.Entry(ventana)
    telefono.grid(row=3, column=1)

    if datos:
        id_com, nombre_val, direccion_val, ciudad_val, telefono_val = datos
        nombre.insert(0, nombre_val)
        direccion.insert(0, direccion_val)
        ciudad.insert(0, ciudad_val)
        telefono.insert(0, telefono_val)

    def guardar():
        payload = {
            "nombre": nombre.get(),
            "direccion": direccion.get(),
            "ciudad": ciudad.get(),
            "telefono": int(telefono.get())
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
root.title("Gestión de barberias")

# Tabla
cols = ("ID", "Nombre", "direccion", "ciudad", "telefono")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=120)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nuevo", command=crear_barberia).pack(side="left", padx=5)
tk.Button(botonera, text="Editar", command=editar_barberia).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar", command=eliminar_barberia).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar", command=recargar_datos).pack(side="left", padx=5)

recargar_datos()
root.mainloop()
