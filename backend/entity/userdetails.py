class UserDetails:
    """
    A class to represent Inventory, any new inventory field in database must be added here
    """
    def __init__(self, **kwargs):
        self.username = kwargs.get("username", None)
        self.password_val = kwargs.get("password_val", None)
        self.firstName = kwargs.get("firstName", None)
        self.lastName = kwargs.get("lastName", None)
        self.region = kwargs.get("region", None)
        self.phone_number = kwargs.get("phone_number", None)
        self.email = kwargs.get("email", None)