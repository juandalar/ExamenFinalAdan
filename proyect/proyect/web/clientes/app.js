async function listarClientes() {
    const res = await fetch(API_BASE + ENDPOINTS.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaClientes");
    lista.innerHTML = "";
    data.forEach(c => {
        const item = document.createElement("li");
        item.textContent = `ID: ${c.id} - ${c.nombre} - ${c.email} - ${c.telefono} - Activo: ${c.activo}`;
        lista.appendChild(item);
    });
}

document.getElementById("formCliente").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        nombre: document.getElementById("nombre").value,
        email: document.getElementById("email").value,
        telefono: document.getElementById("telefono").value,
        password: document.getElementById("password").value
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Cliente registrado.");
    listarClientes();
    mostrarSeccion('lista');
});

async function buscarCliente() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("nombreAccion").value = data.nombre;
        document.getElementById("emailAccion").value = data.email;
        document.getElementById("telefonoAccion").value = data.telefono;
        document.getElementById("passwordAccion").value = "";
        mostrarSeccion('acciones');
        alert("Cliente cargado para edición.");
    } else {
        alert("Cliente no encontrado.");
    }
}

async function actualizarCliente() {
    const id = document.getElementById("idBuscar").value;
    const body = {
        nombre: document.getElementById("nombreAccion").value,
        email: document.getElementById("emailAccion").value,
        telefono: document.getElementById("telefonoAccion").value,
        password: document.getElementById("passwordAccion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarClientes();
    mostrarSeccion('lista');
}

async function eliminarCliente() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarClientes();
    mostrarSeccion('lista');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

listarClientes();
mostrarSeccion('crear');