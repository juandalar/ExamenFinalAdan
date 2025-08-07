
from modulos.barberias.acceso_datos.barberia_dto import BarberiaDTO
from modulos.barberias.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class BarberiaDAOMySQL:
    def guardar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberias (nombre, direccion, telefono, ciudad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (barberia_dto.nombre, barberia_dto.direccion, barberia_dto.telefono, barberia_dto.ciudad))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, ciudad FROM barberias")
            rows = cursor.fetchall()
        return [BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], ciudad=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, ciudad FROM barberias WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], ciudad=row[4])
        return None

    def actualizar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberias SET nombre = %s, direccion = %s, telefono = %s, ciudad = %s WHERE id = %s"
            cursor.execute(sql, (barberia_dto.nombre, barberia_dto.direccion, barberia_dto.telefono, barberia_dto.ciudad, barberia_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberias WHERE id = %s", (id,))
        conn.commit()




class BarberiaDAOPostgres:
    def guardar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO barberias (nombre, direccion, telefono, ciudad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (barberia_dto.nombre, barberia_dto.direccion, barberia_dto.telefono, barberia_dto.ciudad))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, ciudad FROM barberias")
            rows = cursor.fetchall()
        return [BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], ciudad=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, direccion, telefono, ciudad FROM barberias WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return BarberiaDTO(id=row[0], nombre=row[1], direccion=row[2], telefono=row[3], ciudad=row[4])
        return None

    def actualizar(self, barberia_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE barberias SET nombre = %s, direccion = %s, telefono = %s, ciudad = %s WHERE id = %s"
            cursor.execute(sql, (barberia_dto.nombre, barberia_dto.direccion, barberia_dto.telefono, barberia_dto.ciudad, barberia_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM barberias WHERE id = %s", (id,))
        conn.commit()
