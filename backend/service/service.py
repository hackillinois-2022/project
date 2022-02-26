from backend.entity.userdetails import UserDetails
from backend.dao.db_module import DatabaseModule


class Service:
    """
    Service class to serve requests for inventory application
    Functionality :-
    1) Add a record into inventory
    2) Update a record in inventory
    3) Retrieve all the records from inventory
    4) Delete a record from inventory
    5) Restore a record from inventory

    """
    def __init__(self):
        self.db_module = DatabaseModule(True)

    def add_user_data(self, **data):
        """
        Adds user records into databases
        throws error if user id provided is invalid
        :param dict data: dict of all inventory object fields and values
        :return dict response, int status_code: returns the respective response and status code based on input provided
        """
        if not self.validate(data.get("username", "")) or not self.validate(data.get("password", "")):
            return {"message": "Invalid username or password", "successs": False}, 200

        user_data = UserDetails(**data)
        try:
            database_response = self.db_module.insert_user_data(**user_data.__dict__)
            if database_response.rowcount > 0:
                return {"message": "Successfully inserted userdata for username %s" % database_response.inserted_primary_key[0], "successs": True}, 200
            return {"message": "Record for username %s already exists" % data.get("username"), "successs": False}, 200
        except Exception as e:
            print("Error Inserting user record")
            return {"message": "Error Inserting user record", "successs": False}, 200

    #
    # def add_inventory(self, **data):
    #     """
    #     Adds user records into databases
    #     throws error if user id provided is invalid
    #     :param dict data: dict of all inventory object fields and values
    #     :return dict response, int status_code: returns the respective response and status code based on input provided
    #     """
    #     if not self.validate(data.get("id", "")):
    #         return {"message": "Invalid Inventory ID"}, 400
    #     inventory_object = Inventory(**data)
    #     try:
    #         database_response = self.db_module.insert(**inventory_object.__dict__)
    #         if database_response.rowcount > 0:
    #             return {"message": "Successfully inserted inventory for id %s" % database_response.inserted_primary_key[0]}, 200
    #         return {"message": "Record for id %s already exists" % data.get("id")}, 200
    #     except Exception as e:
    #         print("Error Inserting inventory record")
    #         return {"message": "Error Inserting inventory record"}, 500
    #
    # def get_all_inventory(self):
    #     """
    #     Retrieve all Inventory records present
    #     :return dict response, int status_code: returns the respective response and status code based on input provided
    #     """
    #     try:
    #         database_response = self.db_module.get_all()
    #         if database_response.rowcount == 0:
    #             return {"message": "No records found"}, 404
    #         rows = database_response.fetchall()
    #         output = []
    #         for row in rows:
    #             record = dict(row)
    #             record.pop("is_deleted")
    #             record.pop("deletion_comments")
    #             output.append(record)
    #         return output, 200
    #     except Exception as e:
    #         print("Error retrieving records")
    #         return {"message": "Error retrieving records"}, 500
    #
    def get_user_data(self, **data):
        """
        Retrieve User data for specified username
        :param dict data: dict of all inventory object fields and values
        :return dict response, int status_code: returns the respective response and status code based on input provided
        """
        try:
            if not self.validate(data.get("username", "")) or not self.validate(data.get("password", "")):
                return {"message": "Invalid username or password",  "success": False}, 200
            database_response = self.db_module.get_user_details(**data)
            if database_response.rowcount == 0:
                return {"message": "No records found for username %s" % data.get("username"),  "success": False}, 200
            rows = database_response.fetchall()
            output = []
            for row in rows:
                record = dict(row)
                if record.get("password_val", None) != data.get("password_val", ""):
                    return {"message": "password does not match our records", "success": False}, 200
                output.append(record)
            return {"data": output, "success": True}, 200
        except Exception as e:
            print("Error retrieving user data")
            return {"message": "Error retrieving user data", "success": False}, 200

    # def delete_inventory(self, **data):
    #     """
    #     Delete a record from inventory, where a particular field is_deleted is set to 1 (soft delete)
    #     :param dict data: dict of all inventory object fields and values
    #     :return dict response, int status_code: returns the respective response and status code based on input provided
    #     """
    #     try:
    #         if not self.validate(data.get("id", "")):
    #             return {"message": "Invalid Inventory ID"}, 400
    #         database_response = self.db_module.delete(**data)
    #         if database_response.rowcount > 0:
    #             return {"message": "Successfully deleted inventory for id %s" % data.get("id")}, 200
    #         return {"message": "No records found for id %s" % (data.get("id"))}, 404
    #     except Exception as e:
    #         print("Error deleting record")
    #         return {"message": "Error deleting record"}, 500
    #
    # def reverse_delete(self, **data):
    #     """
    #     Restore a record from inventory, where a particular field is_deleted is set to 0 (soft delete restore)
    #     :param dict data: dict of all inventory object fields and values
    #     :return dict response, int status_code: returns the respective response and status code based on input provided
    #     """
    #     try:
    #         if not self.validate(data.get("id", "")):
    #             return {"message": "Invalid Inventory ID"}, 400
    #         database_response = self.db_module.reverse_delete(**data)
    #         if database_response.rowcount > 0:
    #             return {"message": "Successfully restored inventory for id %s" % data.get("id")}, 200
    #         return {"message": "No records found for id %s" % (data.get("id"))}, 404
    #     except Exception as e:
    #         print("Error restoring record")
    #         return {"message": "Error restoring record"}, 500
    #
    # def update_inventory(self, **data):
    #     """
    #     To update inventory for given id
    #     :param dict data: dict of all inventory object fields and values
    #     :return dict response, int status_code: returns the respective response and status code based on input provided
    #     """
    #     try:
    #         if not self.validate(data.get("id", "")):
    #             return {"message": "Invalid Inventory ID"}, 400
    #         database_response = self.db_module.update(**data)
    #         if database_response.rowcount > 0:
    #             return {"message": "Successfully updated inventory for id %s" % data.get("id")}, 200
    #         return {"message": "No records found for id %s" % (data.get("id"))}, 404
    #     except Exception as e:
    #         print("Error updating record")
    #         return {"message": "Error updating record"}, 500
    #
    def validate(self, id):
        """
        To validate inventory id if it's a non negative integer
        :param int id: Inventory id
        :return Bool: True if valid id, else False
        """
        if isinstance(id, str) and len(id) >= 0:
            return True
        return False
