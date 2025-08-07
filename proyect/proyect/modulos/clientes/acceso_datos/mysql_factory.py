from modulos.clientes.acceso_datos.clientes_dao import ClienteDAOMySQL
from modulos.clientes.acceso_datos.dao_factory import ClienteDAOFactory

class MySQLClienteDAOFactory(ClienteDAOFactory):
    def crear_dao(self):
        return ClienteDAOMySQL()