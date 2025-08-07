from modulos.barberias.configuracion.config import cargar_configuracion
from modulos.barberias.acceso_datos.mysql_factory import MySQLBarberiaDAOFactory
from modulos.barberias.acceso_datos.postgres_factory import PostgresBarberiaDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresBarberiaDAOFactory()
    return MySQLBarberiaDAOFactory()