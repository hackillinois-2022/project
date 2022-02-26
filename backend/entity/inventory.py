import datetime


class Produce:
    """
    A class to represent Inventory, any new inventory field in database must be added here
    """
    def __init__(self, **kwargs):
        self.username = kwargs.get("username", None)
        self.cost = kwargs.get("cost", None)
        self.quantity = kwargs.get("quantity", None)
        self.location = kwargs.get("location", None)
        self.produce_name = kwargs.get("produceName", None).lower()
        self.updated = datetime.datetime.now()






