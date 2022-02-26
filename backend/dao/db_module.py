from sqlalchemy import create_engine, MetaData, Table, and_
import backend.utility.utility as utils


class DatabaseModule:
    """
    Module which connects to database and executes queries
    """
    def __init__(self, initialize=False):
        """
        Initialize database engine
        """
        try:
            self.cfg = utils.get_environment_configs()
            print("mysql://%s:%s@%s:%s/%s" % (self.cfg.mysql_user, self.cfg.mysql_password, self.cfg.mysql_host, self.cfg.mysql_port, self.cfg.database))
            self.engine = create_engine(
                "mysql://%s:%s@%s:%s/%s" % (self.cfg.mysql_user, self.cfg.mysql_password, self.cfg.mysql_host, self.cfg.mysql_port, self.cfg.database))
            self.connection = self.engine.connect()
            self.metadata = MetaData()
            if initialize:
                self.__init_table()


        except Exception as e:
            print(e)
            raise Exception("Could not connect to mysql")

    def __init_table(self):
        """
        Initializing ORM table inventory table
        :return: None
        """
        self.user_table = Table(self.cfg.user_table, self.metadata, autoload=True, autoload_with=self.engine)
        self.produce = Table(self.cfg.produce_table, self.metadata, autoload=True, autoload_with=self.engine)

    def __execute(self, query):
        """
        Execute a given query
        :param object query: query to be executed
        :return: query response
        """
        return self.connection.execute(query)

    def insert_user_data(self, **data):
        """
        To build insert query for inventory
        :param dict data: dictionary of inventory object
        :return: query response
        """
        query = self.user_table.insert().values(data).prefix_with("IGNORE")
        return self.__execute(query)

    def insert_produce_data(self, **data):
        """
        To build insert query for inventory
        :param dict data: dictionary of inventory object
        :return: query response
        """
        query = self.produce.insert().values(data).prefix_with("IGNORE")
        return self.__execute(query)

    def get_user_details(self, **data):
        """
        To build get query for a particular inventory
        :param dict data: dictionary of inventory object
        :return: query response
        """
        query = self.user_table.select().where(and_(self.user_table.columns.username == data.get("username")))
        return self.__execute(query)

    def get_produce_data(self, data):
        """
        To build get query for a particular inventory
        :param dict data: dictionary of inventory object
        :return: query response
        """
        query = self.produce.select().where(and_(self.produce.columns.username == data))
        return self.__execute(query)
    #
    # def get_all(self):
    #     """
    #     To build get query for all inventory
    #     :param dict data: dictionary of inventory object
    #     :return: query response
    #     """
    #     query = self.inventory_table.select().where(and_(self.inventory_table.columns.is_deleted == 0))
    #     return self.__execute(query)
    #
    # def update(self, **data):
    #     """
    #     To build update query for a particular inventory
    #     :param dict data: dictionary of inventory object
    #     :return: query response
    #     """
    #     query = self.inventory_table.update().values(data)
    #     query = query.where(and_(self.inventory_table.columns.id == data.get("id"), self.inventory_table.columns.is_deleted == 0))
    #     return self.__execute(query)
    #
    def delete(self, **data):
        """
        To build delete query for a particular inventory where is_deleted is set to 1 to mark it delete (soft delete)
        :param dict data: dictionary of inventory object
        :return: query response
        """
        query = self.produce.delete().where(and_(self.produce.columns.username == data.get("username")), and_(self.produce.columns.produce_name == data.get("produceName").lower()))
        print(query)
        return self.__execute(query)
    #
    # def reverse_delete(self, **data):
    #     """
    #     To build reverse delete query for a particular inventory where is_deleted is set to 0 to mark it delete (soft delete)
    #     :param dict data: dictionary of inventory object
    #     :return: query response
    #     """
    #     query = self.inventory_table.update().values(is_deleted=0)
    #     query = query.where(self.inventory_table.columns.id == data.get("id"))
    #     return self.__execute(query)


