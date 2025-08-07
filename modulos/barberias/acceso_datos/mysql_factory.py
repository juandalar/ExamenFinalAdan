from modulos.barberias.acceso_datos.barberia_dao import BarberiaDAOMySQL
from modulos.barberias.acceso_datos.dao_factory import BarberiaDAOFactory

class MySQLBarberiaDAOFactory(BarberiaDAOFactory):
    def crear_dao(self):
        return BarberiaDAOMySQL()