from modulos.clientes.configuracion.config import cargar_configuracion
from modulos.clientes.acceso_datos.mysql_factory import MySQLClienteDAOFactory
from modulos.clientes.acceso_datos.postgres_factory import PostgresClienteDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresClienteDAOFactory()
    return MySQLClienteDAOFactory()