from modulos.productos.acceso_datos.producto_dao import ProductoDAOMySQL
from modulos.productos.acceso_datos.dao_factory import ProductoDAOFactory

class MySQLProductoDAOFactory(ProductoDAOFactory):
    def crear_dao(self):
        return ProductoDAOMySQL()