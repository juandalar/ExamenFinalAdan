from modulos.clientes.acceso_datos.clientes_dto import ClienteDTO
from modulos.clientes.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class ClienteDAOMySQL:
    def guardar(self, cliente_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nombre, email, telefono, password_hash, activo, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cliente_dto.nombre, cliente_dto.email, cliente_dto.telefono, cliente_dto.password_hash, cliente_dto.activo, cliente_dto.fecha_registro))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes")
            rows = cursor.fetchall()
        return [ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6])
        return None

    def obtener_por_email(self, email):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes WHERE email = %s", (email,))
            row = cursor.fetchone()
        if row:
            return ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6])
        return None

    def actualizar(self, cliente_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE clientes SET nombre = %s, email = %s, telefono = %s, activo = %s WHERE id = %s"
            cursor.execute(sql, (cliente_dto.nombre, cliente_dto.email, cliente_dto.telefono, cliente_dto.activo, cliente_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()

class ClienteDAOPostgres:
    def guardar(self, cliente_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nombre, email, telefono, password_hash, activo, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cliente_dto.nombre, cliente_dto.email, cliente_dto.telefono, cliente_dto.password_hash, cliente_dto.activo, cliente_dto.fecha_registro))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes")
            rows = cursor.fetchall()
        return [ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6])
        return None

    def obtener_por_email(self, email):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email, telefono, password_hash, activo, fecha_registro FROM clientes WHERE email = %s", (email,))
            row = cursor.fetchone()
        if row:
            return ClienteDTO(id=row[0], nombre=row[1], email=row[2], telefono=row[3], password_hash=row[4], activo=row[5], fecha_registro=row[6])
        return None

    def actualizar(self, cliente_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE clientes SET nombre = %s, email = %s, telefono = %s, activo = %s WHERE id = %s"
            cursor.execute(sql, (cliente_dto.nombre, cliente_dto.email, cliente_dto.telefono, cliente_dto.activo, cliente_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()