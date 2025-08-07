import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("modulos/comentarios/configuracion/config.json") as f:
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
                    c["id"], c["usuario_email"], c["texto"], c["calificacion"], c.get("fecha", "")
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_comentario():
    dialogo_comentario("Crear nuevo comentario")

def editar_comentario():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un comentario.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_comentario("Editar comentario", valores)

def eliminar_comentario():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione un comentario.")
        return
    id_com = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este comentario?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(id_com)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "Comentario eliminado.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def dialogo_comentario(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)

    tk.Label(ventana, text="Email:").grid(row=0, column=0)
    email = tk.Entry(ventana)
    email.grid(row=0, column=1)

    tk.Label(ventana, text="Comentario:").grid(row=1, column=0)
    texto = tk.Entry(ventana)
    texto.grid(row=1, column=1)

    tk.Label(ventana, text="Calificación:").grid(row=2, column=0)
    calificacion = tk.Entry(ventana)
    calificacion.grid(row=2, column=1)

    if datos:
        id_com, email_val, texto_val, calif_val, _ = datos
        email.insert(0, email_val)
        texto.insert(0, texto_val)
        calificacion.insert(0, calif_val)

    def guardar():
        payload = {
            "usuario_email": email.get(),
            "texto": texto.get(),
            "calificacion": calificacion.get()
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

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, columnspan=2)

# Ventana principal
root = tk.Tk()
root.title("Gestión de Comentarios")

# Tabla
cols = ("ID", "Email", "Comentario", "Calificación", "Fecha")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nuevo", command=crear_comentario).pack(side="left", padx=5)
tk.Button(botonera, text="Editar", command=editar_comentario).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar", command=eliminar_comentario).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar", command=recargar_datos).pack(side="left", padx=5)

recargar_datos()
root.mainloop()
