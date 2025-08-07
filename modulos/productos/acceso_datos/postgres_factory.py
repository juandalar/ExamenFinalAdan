from modulos.productos.acceso_datos.producto_dao import ProductoDAOPostgres
from modulos.productos.acceso_datos.dao_factory import ProductoDAOFactory

class PostgresProductoDAOFactory(ProductoDAOFactory):
    def crear_dao(self):
        return ProductoDAOPostgres()