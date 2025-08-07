from modulos.clientes.acceso_datos.clientes_dao import ClienteDAOPostgres
from modulos.clientes.acceso_datos.dao_factory import ClienteDAOFactory

class PostgresClienteDAOFactory(ClienteDAOFactory):
    def crear_dao(self):
        return ClienteDAOPostgres()