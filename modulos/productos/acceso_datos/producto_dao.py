
from modulos.productos.acceso_datos.producto_dto import ProductoDTO
from modulos.productos.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class ProductoDAOMySQL:
    def guardar(self, producto_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO productos (nombre, descripcion, precio, categoria) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.categoria))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, categoria FROM productos")
            rows = cursor.fetchall()
        return [ProductoDTO(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], categoria=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, categoria FROM productos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ProductoDTO(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], categoria=row[4])
        return None

    def actualizar(self, producto_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, categoria = %s WHERE id = %s"
            cursor.execute(sql, (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.categoria, producto_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
        conn.commit()




class ProductoDAOPostgres:
    def guardar(self, producto_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO productos (nombre, descripcion, precio, categoria) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.categoria))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, categoria FROM productos")
            rows = cursor.fetchall()
        return [ProductoDTO(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], categoria=row[4]) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio, categoria FROM productos WHERE id = %s", (id,))
            row = cursor.fetchone()
        if row:
            return ProductoDTO(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], categoria=row[4])
        return None

    def actualizar(self, producto_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, categoria = %s WHERE id = %s"
            cursor.execute(sql, (producto_dto.nombre, producto_dto.descripcion, producto_dto.precio, producto_dto.categoria, producto_dto.id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
        conn.commit()
