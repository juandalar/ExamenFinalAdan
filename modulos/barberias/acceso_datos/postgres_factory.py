from modulos.barberias.acceso_datos.barberia_dao import BarberiaDAOPostgres
from modulos.barberias.acceso_datos.dao_factory import BarberiaDAOFactory

class PostgresBarberiaDAOFactory(BarberiaDAOFactory):
    def crear_dao(self):
        return BarberiaDAOPostgres()