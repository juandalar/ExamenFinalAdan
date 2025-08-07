from modulos.productos.configuracion.config import cargar_configuracion
from modulos.productos.acceso_datos.mysql_factory import MySQLProductoDAOFactory
from modulos.productos.acceso_datos.postgres_factory import PostgresProductoDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresProductoDAOFactory()
    return MySQLProductoDAOFactory()