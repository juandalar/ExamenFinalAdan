
from modulos.barberos.acceso_datos.barbero_dto import BarberoDTO
from modulos.barberos.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class BarberoDAOMySQL:
    def guardar(self, barbero_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberos (nombre, correo, telefono, especialidad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (barbero_dto.nombre, barbero_dto.correo, barbero_dto.telefono, barbero_dto.especialidad))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, correo, telefono, especialidad FROM barberos")
            rows = cursor.fetchall()
        return [BarberoDTO(id=row[0], nombre=row[1], correo=row[2], telefono=row[3], especialidad=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, correo, telefono, especialidad FROM barberos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberoDTO(id=row[0], nombre=row[1], correo=row[2], telefono=row[3], especialidad=row[4])
        return None

    def actualizar(self, barbero_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberos SET nombre = %s, correo = %s, telefono = %s, especialidad = %s WHERE id = %s"
            cursor.execute(sql, (barbero_dto.nombre, barbero_dto.correo, barbero_dto.telefono, barbero_dto.especialidad, barbero_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberos WHERE id = %s", (id,))
        conn.commit()




class BarberoDAOPostgres:
    def guardar(self, barbero_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberos (nombre, correo, telefono, especialidad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (barbero_dto.nombre, barbero_dto.correo, barbero_dto.telefono, barbero_dto.especialidad))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, correo, telefono, especialidad FROM barberos")
            rows = cursor.fetchall()
        return [BarberoDTO(id=row[0], nombre=row[1], correo=row[2], telefono=row[3], especialidad=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, correo, telefono, especialidad FROM barberos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberoDTO(id=row[0], nombre=row[1], correo=row[2], telefono=row[3], especialidad=row[4])
        return None

    def actualizar(self, barbero_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberos SET nombre = %s, correo = %s, telefono = %s, especialidad = %s WHERE id = %s"
            cursor.execute(sql, (barbero_dto.nombre, barbero_dto.correo, barbero_dto.telefono, barbero_dto.especialidad, barbero_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberos WHERE id = %s", (id,))
        conn.commit()
