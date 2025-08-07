from modulos.barberos.acceso_datos.barbero_dao import BarberoDAOMySQL
from modulos.barberos.acceso_datos.dao_factory import BarberoDAOFactory

class MySQLBarberoDAOFactory(BarberoDAOFactory):
    def crear_dao(self):
        return BarberoDAOMySQL()