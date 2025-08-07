from modulos.barberos.acceso_datos.barbero_dao import BarberoDAOPostgres
from modulos.barberos.acceso_datos.dao_factory import BarberoDAOFactory

class PostgresBarberoDAOFactory(BarberoDAOFactory):
    def crear_dao(self):
        return BarberoDAOPostgres()