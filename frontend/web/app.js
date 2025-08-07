
// Comentarios
async function listarComentarios() {
    const res = await fetch(API_BASE + ENDPOINTS.comentarios.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaComentarios");
    lista.innerHTML = "";
    data.forEach(c => {
        const item = document.createElement("li");
        item.textContent = `ID: ${c.id} - ${c.usuario_email} - ${c.texto} (${c.calificacion})`;
        lista.appendChild(item);
    });
}

document.getElementById("formComentario").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        texto: document.getElementById("texto").value,
        usuario_email: document.getElementById("email").value,
        calificacion: parseInt(document.getElementById("calificacion").value)
    };
    await fetch(API_BASE + ENDPOINTS.comentarios.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Comentario creado.");
    listarComentarios();
    mostrarSeccion('listaComentarios');
});

async function buscarComentario() {
    const id = document.getElementById("idBuscarComentario").value;
    const res = await fetch(API_BASE + ENDPOINTS.comentarios.read_one(id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("textoAccion").value = data.texto;
        document.getElementById("emailAccion").value = data.usuario_email;
        document.getElementById("calificacionAccion").value = data.calificacion;
        mostrarSeccion('accionesComentario');
        alert("Comentario cargado para edición.");
    } else {
        alert("Comentario no encontrado.");
    }
}

async function actualizarComentario() {
    const id = document.getElementById("idBuscarComentario").value;
    const body = {
        texto: document.getElementById("textoAccion").value,
        usuario_email: document.getElementById("emailAccion").value,
        calificacion: parseInt(document.getElementById("calificacionAccion").value)
    };
    const res = await fetch(API_BASE + ENDPOINTS.comentarios.update(id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarComentarios();
    mostrarSeccion('listaComentarios');
}

async function eliminarComentario() {
    const id = document.getElementById("idBuscarComentario").value;
    const res = await fetch(API_BASE + ENDPOINTS.comentarios.delete(id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarComentarios();
    mostrarSeccion('listaComentarios');
}

// Productos
async function listarProductos() {
    const res = await fetch(API_BASE + ENDPOINTS.productos.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaProductos");
    lista.innerHTML = "";
    data.forEach(p => {
        const item = document.createElement("li");
        item.textContent = `ID: ${p.id} - ${p.categoria} - ${p.nombre} - ${p.descripcion} (${p.precio})`;
        lista.appendChild(item);
    });
}

document.getElementById("formProducto").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        nombre: document.getElementById("nombre").value,
        descripcion: document.getElementById("descripcion").value,
        categoria: document.getElementById("categoria").value,
        precio: parseInt(document.getElementById("precio").value)
    };
    await fetch(API_BASE + ENDPOINTS.productos.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Producto creado.");
    listarProductos();
    mostrarSeccion('listaProductos');
});

async function buscarProducto() {
    const id = document.getElementById("idBuscarProducto").value;
    const res = await fetch(API_BASE + ENDPOINTS.productos.read_one(id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("nombreAccion").value = data.nombre;
        document.getElementById("descripcionAccion").value = data.descripcion;
        document.getElementById("categoriaAccion").value = data.categoria;
        document.getElementById("precioAccion").value = data.precio;
        mostrarSeccion('accionesProducto');
        alert("Producto cargado para edición.");
    } else {
        alert("Producto no encontrado.");
    }
}

async function actualizarProducto() {
    const id = document.getElementById("idBuscarProducto").value;
    const body = {
        nombre: document.getElementById("nombreAccion").value,
        descripcion: document.getElementById("descripcionAccion").value,
        precio: parseInt(document.getElementById("precioAccion").value),
        categoria: document.getElementById("categoriaAccion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.productos.update(id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarProductos();
    mostrarSeccion('listaProductos');
}

async function eliminarProducto() {
    const id = document.getElementById("idBuscarProducto").value;
    const res = await fetch(API_BASE + ENDPOINTS.productos.delete(id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarProductos();
    mostrarSeccion('listaProductos');
}

// Barberos
async function listarBarberos() {
    const res = await fetch(API_BASE + ENDPOINTS.barberos.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaBarberos");
    lista.innerHTML = "";
    data.forEach(p => {
        const item = document.createElement("li");
        item.textContent = `ID: ${p.id} - ${p.especialidad} - ${p.nombre} - ${p.correo} (${p.telefono})`;
        lista.appendChild(item);
    });
}

document.getElementById("formBarbero").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        nombre: document.getElementById("nombreBarbero").value,
        correo: document.getElementById("correo").value,
        especialidad: document.getElementById("especialidad").value,
        telefono: parseInt(document.getElementById("telefono").value)
    };
    await fetch(API_BASE + ENDPOINTS.barberos.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Barbero creado.");
    listarBarberos();
    mostrarSeccion('listaBarberos');
});

async function buscarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    const res = await fetch(API_BASE + ENDPOINTS.barberos.read_one(id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("nombreBarberoAccion").value = data.nombre;
        document.getElementById("correoAccion").value = data.correo;
        document.getElementById("especialidadAccion").value = data.especialidad;
        document.getElementById("telefonoAccion").value = data.telefono;
        mostrarSeccion('accionesBarbero');
        alert("Barbero cargado para edición.");
    } else {
        alert("Barbero no encontrado.");
    }
}

async function actualizarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    const body = {
        nombre: document.getElementById("nombreBarberoAccion").value,
        correo: document.getElementById("correoAccion").value,
        especialidad: document.getElementById("especialidadAccion").value,
        telefono: parseInt(document.getElementById("telefonoAccion").value)
    };
    const res = await fetch(API_BASE + ENDPOINTS.barberos.update(id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarBarberos();
    mostrarSeccion('listaBarberos');
}

async function eliminarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    const res = await fetch(API_BASE + ENDPOINTS.barberos.delete(id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarBarberos();
    mostrarSeccion('listaBarberos');
}

// Barberias
async function listarBarberias() {
    const res = await fetch(API_BASE + ENDPOINTS.barberias.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaBarberias");
    lista.innerHTML = "";
    data.forEach(p => {
        const item = document.createElement("li");
        item.textContent = `ID: ${p.id} - ${p.ciudad} - ${p.nombre} - ${p.direccion} (${p.telefono})`;
        lista.appendChild(item);
    });
}

document.getElementById("formBarberia").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        nombre: document.getElementById("nombreBarberia").value,
        direccion: document.getElementById("direccion").value,
        ciudad: document.getElementById("ciudad").value,
        telefono: parseInt(document.getElementById("telefonoBarberia").value)
    };
    await fetch(API_BASE + ENDPOINTS.barberias.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Barberia creado.");
    listarBarberias();
    mostrarSeccion('listaBarberias');
});

async function buscarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    const res = await fetch(API_BASE + ENDPOINTS.barberias.read_one(id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("nombreBarberiaAccion").value = data.nombre;
        document.getElementById("direccionAccion").value = data.direccion;
        document.getElementById("ciudadAccion").value = data.ciudad;
        document.getElementById("telefonoBarberiaAccion").value = data.telefono;
        mostrarSeccion('accionesBarberia');
        alert("Barberia cargada para edición.");
    } else {
        alert("Barberia no encontrado.");
    }
}

async function actualizarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    const body = {
        nombre: document.getElementById("nombreBarberiaAccion").value,
        direccion: document.getElementById("direccionAccion").value,
        telefono: parseInt(document.getElementById("telefonoBarberiaAccion").value),
        ciudad: document.getElementById("ciudadAccion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.barberias.update(id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarBarberias();
    mostrarSeccion('listaBarberias');
}

async function eliminarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    const res = await fetch(API_BASE + ENDPOINTS.barberias.delete(id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarBarberias();
    mostrarSeccion('listaBarberias');
}

// Mostrar Secciones
function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

// Inicio
listarComentarios();
listarProductos();
listarBarberos();
listarBarberias();
mostrarSeccion('crearComentario');