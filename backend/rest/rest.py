from flask import Flask, request, Response
from flask_restful import Resource, Api
import json

from backend.service.service import Service

service = Service()

app = Flask("inventory_service")
api = Api(app)


class Authenticate(Resource):
    """
    Flask Rest Service Resource to support single id requests
    """
    # @staticmethod
    # def put():
    #     """
    #     Using HTTP PUT method to update an inventory record
    #     :return Response_object: Success or failure message
    #     """
    #     try:
    #         request_data = request.get_data()
    #         response = Response()
    #         if not request_data:
    #             response.data = json.dumps({"message": "No input data to process"})
    #             response.status_code = 400
    #             return response
    #
    #         request_data = json.loads(request_data)
    #         output_data, response.status_code = service.update_inventory(**request_data)
    #         response.data = json.dumps(output_data, default=str)
    #         return response
    #     except Exception as e:
    #         print("Error while parsing data")
    #         print(e.args)
    #         response = Response(status=400)
    #         response.data = json.dumps({"message": "Error while parsing data"})
    #         return response

    @staticmethod
    def post():
        """
        Using HTTP POST method to insert an inventory record
        :return : Response_object: Success or failure message
        """
        try:
            request_data = request.get_data()
            response = Response()
            if not request_data:
                response.data = json.dumps({"message": "No input data to process"})
                response.status_code = 400
                return response
            request_data = json.loads(request_data)
            output_data, response.status_code = service.add_user_data(**request_data)
            response.data = json.dumps(output_data, default=str)
            return response
        except Exception as e:
            print("Error while parsing data")
            print(e.args)
            response = Response(status=400)
            response.data = json.dumps({"message": "Error while parsing data"})
            return response

    # @staticmethod
    # def delete():
    #     """
    #     Using HTTP Delete method to delete an inventory record
    #     :return : Response_object: Success or failure message
    #     """
    #     try:
    #         request_data = request.get_data()
    #         response = Response()
    #         if not request_data:
    #             response.data = json.dumps({"message": "No input data to process"})
    #             response.status_code = 400
    #             return response
    #
    #         request_data = json.loads(request_data)
    #         output_data, response.status_code = service.delete_inventory(**request_data)
    #         response.data = json.dumps(output_data, default=str)
    #         return response
    #
    #     except Exception as e:
    #         print("Error while parsing data")
    #         print(e.args)
    #         response = Response(status=400)
    #         response.data = json.dumps({"message": "Error while parsing data"})
    #         return response

    @staticmethod
    def get():
        """
        Using HTTP Get method to retrieve an inventory record
        :return : Response_object: inventory record or failure message
        """
        try:
            request_data = request.get_data()
            response = Response()
            if not request_data:
                response.data = json.dumps({"message": "No input data to process"})
                response.status_code = 400
                return response

            request_data = json.loads(request_data)
            output_data, response.status_code = service.get_user_data(**request_data)
            response.data = json.dumps(output_data, default=str)
            return response
        except Exception as e:
            print("Error while parsing data")
            print(e.args)
            response = Response(status=400)
            response.data = json.dumps({"message": "Error while parsing data"})
            return response


# class InventoryAll(Resource):
#     @staticmethod
#     def get():
#         """
#         Using HTTP Get method to retrieve all inventory records
#         :return : Response_object: inventory records or failure message
#         """
#         try:
#             response = Response()
#             output_data, response.status_code = service.get_all_inventory()
#             response.data = json.dumps(output_data, default=str)
#             return response
#         except Exception as e:
#             print("Error while parsing data")
#             print(e.args)
#             response = Response(status=400)
#             response.data = json.dumps({"message": "Error while parsing data"})
#             return response
#
#
# class InventoryUndo(Resource):
#     @staticmethod
#     def put():
#         """
#         Using HTTP PUT method to restore a deleted record
#         :return : Response_object: Success or failure message
#         """
#         try:
#             request_data = request.get_data()
#             response = Response()
#             if not request_data:
#                 response.data = json.dumps({"message": "No input data to process"})
#                 response.status_code = 400
#                 return response
#
#             request_data = json.loads(request_data)
#             output_data, response.status_code = service.reverse_delete(**request_data)
#             response.data = json.dumps(output_data, default=str)
#             return response
#
#         except Exception as e:
#             print("Error while parsing data")
#             print(e.args)
#             response = Response(status=400)
#             response.data = json.dumps({"message": "Error while parsing data"})
#             return response


api.add_resource(Authenticate, "/authenticate")
# api.add_resource(InventoryAll, "/inventory/all")
# api.add_resource(InventoryUndo, "/inventory/undo")

